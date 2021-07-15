class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        mi = max(weights)
        ma = sum(weights)
        
        def canFit(cap):
            num = 1
            re = cap 
            for i in range(len(weights)):
                x = weights[i]
                if x > re:
                    re = cap 
                    num += 1
                re -= x
            return num <= D
        
        while mi < ma:
            mid = mi + (ma - mi) // 2
            if canFit(mid):
                ma = mid
            else:
                mi = mid+1
        return mi
