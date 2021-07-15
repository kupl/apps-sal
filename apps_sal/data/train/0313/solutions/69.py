class Solution:
    def minDays(self, bloomDay, m, k):
        
        if m * k > len(bloomDay): return -1
            
        def canBloom(cand):
            bloomed = 0
            bouquet = 0
            for i in range(len(bloomDay)):
                if bloomDay[i] > cand:
                    bouquet = 0
                else:
                    bouquet += 1
                    if bouquet == k:
                        bloomed += 1
                        bouquet = 0
            return bloomed>=m

        l, r = min(bloomDay), max(bloomDay)
        while l < r:
            mid = l + (r - l) // 2
            if canBloom(mid):
                r = mid
            else:
                l = mid + 1
        return l
