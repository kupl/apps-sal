class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < m * k:
            return -1

        def canMake(days, bloomDay, k):
            flowers, n = 0, 0
            for bloom in bloomDay:
                if bloom > days:
                    flowers = 0
                else:
                    n = n + (flowers + 1) // k
                    flowers = (flowers + 1) % k
            return n

        # use binary search. search values are
        # within min(bloomDay) and max(bloomDay)
        l, r = min(bloomDay), max(bloomDay)
        while l <= r:
            mid = l + (r - l) // 2
            count = canMake(mid, bloomDay, k)
            if count == m:
                r = mid - 1
            elif count < m:
                l = mid + 1
            elif count > m:
                r = mid - 1
        return l
