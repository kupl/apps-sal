class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m*k > len(bloomDay):
            return -1
        
        def canMakeBouquets(cap):
            nBouquets = 0
            nFlowers = 0
            for i in range(len(bloomDay)):
                if bloomDay[i] > cap:
                    nFlowers = 0
                    continue
                nFlowers += 1
                if nFlowers == k:
                    nBouquets += 1
                    nFlowers = 0
            return nBouquets >= m
        
        lo, hi = min(bloomDay), max(bloomDay)
        while lo < hi:
            med = lo + (hi-lo)//2
            if canMakeBouquets(med):
                hi = med
            else:
                lo = med + 1
        return hi
