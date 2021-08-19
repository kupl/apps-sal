class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def canMakeBouquets(blooms: List[bool], m: int, k: int) -> bool:
            bouqs_to_fit = m
            run = 0
            for f in blooms:
                if f:
                    run += 1
                else:
                    run = 0
                if run == k:
                    bouqs_to_fit -= 1  # fit a bouquet
                    run = 0
            return bouqs_to_fit <= 0
        if len(bloomDay) < m * k:
            return -1

        candidates = sorted(set(bloomDay))

        lo = 0
        hi = len(candidates) - 1
        while(lo < hi):
            mid = (lo + hi) // 2
            if canMakeBouquets(map(lambda x: x <= candidates[mid], bloomDay), m, k):
                hi = mid
            else:
                lo = mid + 1
        return candidates[lo]
