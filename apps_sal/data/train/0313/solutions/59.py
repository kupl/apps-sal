class Solution:

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < m * k:
            return -1
        (min_day, max_day) = (min(bloomDay), max(bloomDay))
        while min_day <= max_day:
            mid = min_day + (max_day - min_day) // 2
            if self.check(bloomDay, mid, m, k):
                if max_day == mid:
                    return max_day
                max_day = mid
            else:
                min_day = mid + 1
        return max_day

    def check(self, bloomDay, day, m, k):
        un_m = 0
        last_bloom = -1
        n_before_bloom = 0
        for (i, d) in enumerate(bloomDay):
            if d <= day:
                n_before_bloom += 1
                last_bloom = i
                if n_before_bloom >= k:
                    un_m += 1
                    n_before_bloom -= k
            else:
                n_before_bloom = 0
        return un_m >= m
