class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def condition(day) -> bool:
            a = 0
            b = 0
            for bloom in bloomDay:
                if bloom <= day:
                    a += 1
                else:
                    b += a // k
                    a = 0
            b += a // k
            return b >= m

        if len(bloomDay) < m * k:
            return -1

        left, right = 1, max(bloomDay)  # could be [0, n], [1, n] etc. Depends on problem
        while left < right:
            mid = (left + right) // 2
            if condition(mid):
                right = mid
            else:
                left = mid + 1
        return left
