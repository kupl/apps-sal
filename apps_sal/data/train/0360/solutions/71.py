class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        def possible(cap):
            d = D
            i = 0
            while i < len(weights) and weights[i] <= cap:
                cur = 0
                while i < len(weights) and cur + weights[i] <= cap:
                    cur += weights[i]
                    i += 1
                d -= 1
            
            if i < len(weights):
                return False
            return d >= 0
            
        total = sum(weights)
        
        l, r = 1, total
        ans = float('inf')
        
        while l <= r:
            m = l + (r-l)//2
            
            if possible(m):
                r = m - 1
                ans = min(ans, m)
            else:
                l = m + 1
        return ans
