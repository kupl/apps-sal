class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        
        def test_ship_weights(capacity):
            dq = collections.deque(weights)
            for day in range(D):
                daily_capacity = capacity
                while dq and dq[0] <= daily_capacity:
                    daily_capacity -=  dq.popleft()
                
            if dq: return False
            else: return True
            
        l, r = 0, sum(weights)
        
        while l<r:
            m = (l+r) //2 + 1
            if test_ship_weights(m):
                r = m-1
            else:
                l = m+1
        if test_ship_weights(l): return l
        if test_ship_weights(r): return r
        if test_ship_weights(m): return m
        else:
            return r + 1
        # val = test_ship_weights(l)
        # if val==False: 
        #     if test_ship_weights(r): 
        #         return r
        return l
        

        

