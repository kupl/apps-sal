class Solution:
    def minDays(self, b: List[int], m: int, k: int) -> int:
        if m*k > len(b):
            return -1
        l,r = min(b), max(b)
        def possible(days):
            bonquets, flowers = 0, 0
            for bloom in b:
                if bloom > days:
                    flowers = 0
                else:
                    flowers += 1
                if flowers == k:
                    flowers = 0
                    bonquets += 1
            return bonquets >= m
            
        while l<r:
            mi = (l+r)//2
            
            if possible(mi):
                r = mi
            else:
                l = mi+1
        return l
