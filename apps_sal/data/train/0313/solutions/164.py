class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def feasible(day):
            bouquets = 0
            adjacent = 0
            for bloom in bloomDay:
                if bloom > day:
                    adjacent = 0
                else:
                    adjacent += 1

                if adjacent == k:
                    bouquets += 1
                    adjacent = 0

            return bouquets >= m

        left, right = min(bloomDay), max(bloomDay)
        while left < right:
            mid = left + (right - left) // 2
            if feasible(mid):
                right = mid
            else:
                left = mid + 1

        return left if feasible(left) else -1
