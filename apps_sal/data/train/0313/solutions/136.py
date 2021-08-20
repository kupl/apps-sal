class Solution:

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        bloomDayDict = defaultdict(list)
        for (i, v) in enumerate(bloomDay):
            bloomDayDict[v].append(i)

        def feasible(days) -> bool:
            (bonquets, flowers) = (0, 0)
            for bloom in bloomDay:
                if bloom > days:
                    flowers = 0
                else:
                    bonquets += (flowers + 1) // k
                    flowers = (flowers + 1) % k
            return bonquets >= m
        (left, right) = (1, max(bloomDay))
        while left < right:
            mid = left + (right - left) // 2
            if feasible(mid):
                right = mid
            else:
                left = mid + 1
        return left if feasible(left) else -1
