class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        def calDays(weights, cap):
            days = 1
            acc_w = 0
            for w in weights:
                acc_w += w
                if acc_w > cap:
                    days += 1
                    acc_w = w
            return days
            
        lo = max(weights)
        hi = lo * len(weights) // D
        while lo < hi:
            med = lo + (hi-lo)//2
            days = calDays(weights, med)
            if days <= D:
                hi = med
            else:
                lo = med+1
        return hi

