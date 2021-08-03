class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        if k * m > len(bloomDay):
            return -1

        unique_bloom_days = sorted(set(bloomDay))

        lo = 0
        hi = len(unique_bloom_days) - 1

        if hi == 0:
            return unique_bloom_days[0]

        while True:
            curr_idx = int((lo + hi) / 2)
            if curr_idx == lo:
                idx = curr_idx
            curr_day = unique_bloom_days[curr_idx]
            # check if the condition is satisfiable
            bouquet = 0
            curr = 0
            for i in range(len(bloomDay)):
                if bloomDay[i] <= curr_day:
                    curr += 1
                    if curr >= k:
                        bouquet += 1
                        curr = 0
                else:
                    curr = 0

            if bouquet < m:  # not enough
                if curr_idx == lo:
                    idx = lo + 1
                    break
                else:
                    lo = curr_idx
            else:  # enough
                hi = curr_idx
                if hi == lo:
                    idx = hi
                    break
        return unique_bloom_days[idx]
