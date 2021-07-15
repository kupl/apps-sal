class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        
        SUM = sum(weights)
        MAX = max(weights)
        h = SUM
        l = max(MAX, SUM // D) - 1
        
        def canDo(arr, D, num):
            j = 0
            for i in range(D):
                # can ship a pool
                total = 0
                while j < len(arr) and total + arr[j] <= num:
                    total += arr[j]
                    j += 1
                if j == len(arr):
                    return True
                elif total == 0:
                    return False
            return j == len(arr)
        
        while h > l + 1:
            m = (l + h) // 2
            if canDo(weights, D, m):
                h = m
            else:
                l = m
        return l + 1
