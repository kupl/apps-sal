class Solution:

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        def feasible(days):
            flower = 0
            boq = 0
            for bloom in bloomDay:
                if bloom > days:
                    flower = 0
                else:
                    boq = boq + (flower + 1) // k
                    flower = (flower + 1) % k
            if boq >= m:
                return True
            return False
        if len(bloomDay) < m * k:
            return -1
        low = min(bloomDay)
        high = max(bloomDay)
        while low < high:
            mid = (low + high) // 2
            if feasible(mid):
                high = mid
            else:
                low = mid + 1
        return low
