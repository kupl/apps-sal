class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        
        def condition(minWeight):
            dayCt = 1
            curWeight = 0
            for i, w in enumerate(weights):
                if curWeight + w <= minWeight:
                    curWeight += w
                else:
                    dayCt += 1
                    curWeight = w
            
            return dayCt <= D
        
        l = max(weights)
        r = sum(weights)
        
        while l < r:
            m = l + (r - l) // 2
            if condition(m):
                r = m
            else:
                l = m + 1
        
        return l

