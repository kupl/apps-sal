class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        l, h = max(weights), sum(weights)
        total = h
        
        while l <= h:
            m = (l + h) // 2
            days, count, t = D, 0, 0
            for w in weights:
                if days == 0:
                    break
                if count + w > m:
                    count = w
                    days -= 1
                else:
                    count += w
                t += w
            
            if t == total and days > 0:
                h = m - 1
            else:
                l = m + 1
        return l
