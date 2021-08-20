class Solution:

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        def feasible(largest):
            (cur_len, made) = (0, 0)
            for bloom in bloomDay:
                if bloom > largest:
                    cur_len = 0
                    continue
                cur_len += 1
                if cur_len == k:
                    made += 1
                    cur_len = 0
                if made == m:
                    return True
            return False
        if len(bloomDay) < k * m:
            return -1
        (left, right) = (1, max(bloomDay))
        while left < right:
            mid = (left + right) // 2
            if feasible(mid):
                right = mid
            else:
                left = mid + 1
        return left
