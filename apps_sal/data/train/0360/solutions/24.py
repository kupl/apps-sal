class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        
        # dp [i][d]
        # dp [0][d] = w [0]
        # dp [i][d] = max (w [i], dp [i-1][d-1]) 
        #             min (dp [i-j][d-1] + sum (w [j: i]))
        # dp [i][d] = max (
        #                 min (
        #                   dp [i-j][d-1] + sum (w [i-j+1: i+1]) ,   j >= 1    
        #                 ))
        # O (n*n*D)
        
        # binary search 
        # O (n log n)
        
        n = len (weights)
        def canShipWithCap (cap):
            d = 1
            w = 0
            for i in range (0, n):
                if weights [i] + w <= cap:
                    w += weights [i]
                else: 
                    w = weights [i]
                    d += 1
                    if d > D: return False
            return True
        
        high = sum (weights)
        low = max (weights)
        
        while low < high:
            
            mid = low + (high - low) // 2
            if canShipWithCap (mid): high = mid 
            else: low = mid + 1
            
        return low
        

