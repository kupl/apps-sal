class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        def can_make(days):
            num_boqs = 0
            num_flows = 0

            start = 0

            for bloom in bloomDay:
                if bloom > days:
                    num_flows = 0
                else:
                    num_boqs += (num_flows + 1) // k
                    num_flows = (num_flows + 1) % k

            return num_boqs >= m

        if len(bloomDay) < m * k:
            return -1

        left, right = 1, max(bloomDay)
        while left < right:
            mid = left + (right - left) // 2
            if can_make(mid):
                right = mid
            else:
                left = mid + 1

        return left
