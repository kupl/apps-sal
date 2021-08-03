class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        def possible(x):
            flo, bq = 0, 0
            for bloom in bloomDay:
                if bloom > x:
                    flo = 0
                else:
                    flo += 1
                    if flo >= k:
                        flo = 0
                        bq += 1
            return bq >= m

        if m * k > len(bloomDay):
            return -1

        left, right = 1, max(bloomDay)
        while left < right:
            mid = (left + right) // 2
            if possible(mid):
                right = mid
            else:
                left = mid + 1
        return left
