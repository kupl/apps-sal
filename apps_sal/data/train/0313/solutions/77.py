class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < m * k:
            return -1

        def feasible(day):
            flowers, bouquets = 0, 0
            for bloom in bloomDay:
                if bloom > day:
                    flowers = 0
                else:
                    bouquets += (flowers + 1) // k
                    flowers = (flowers + 1) % k
            return bouquets >= m

        l, r = 1, max(bloomDay)
        while l < r:
            mid = (l + r) // 2
            if feasible(mid):
                r = mid
            else:
                l = mid + 1
        return l
