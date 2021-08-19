class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if m * k > n:
            return -1

        def can_make_bouquets(m: int, k: int, day: int) -> bool:
            #print(m, k, day)
            total_bouquets = 0
            curr_flowers = 0
            for index, d in enumerate(bloomDay):
                if total_bouquets + 1 + (n - index - 1) // k < m:
                    # print(\"No\")
                    return False
                if d <= day:
                    curr_flowers += 1
                    if curr_flowers == k:
                        total_bouquets += 1
                        curr_flowers = 0
                else:
                    curr_flowers = 0
                if total_bouquets == m:
                    # print(\"Yes\")
                    return True
            return False

        days = sorted(list(set(bloomDay)))
        lo, hi = 0, len(days) - 1
        min_days = float('inf')
        # print(days)
        while lo <= hi:
            mi = (lo + hi) // 2
            #print(lo, mi, hi)
            if can_make_bouquets(m, k, days[mi]):
                min_days = min(min_days, days[mi])
                hi = mi - 1
            else:
                lo = mi + 1

        return min_days if min_days < float('inf') else -1
