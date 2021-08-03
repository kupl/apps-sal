class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < m * k:
            return -1

        left, right = 1, max(bloomDay)
        while left < right:
            mid = left + (right - left) // 2
            if self.__feasible(bloomDay, k, m, mid):
                right = mid
            else:
                left = mid + 1
        return left

    def __feasible(self, bloomDay, k, m, day):
        bloom = [day >= bloom_day for bloom_day in bloomDay]
        cnt = 0
        accu = 0
        for b in bloom:
            if b:
                accu += 1
                if accu == k:
                    cnt += 1
                    accu = 0
            else:
                accu = 0
        return cnt >= m
