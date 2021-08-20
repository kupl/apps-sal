class Solution:

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        def check(flower, N, m, k):
            count = 0
            for i in flower:
                if i == 1:
                    count += 1
                    if count == k:
                        m -= 1
                        count = 0
                    if m == 0:
                        return True
                else:
                    count = 0
            return False
        N = len(bloomDay)
        if N < m * k:
            return -1
        left = 0
        right = max(bloomDay)
        res = right
        while left < right:
            day = (left + right) // 2
            flower = [0] * N
            for x in range(N):
                if bloomDay[x] <= day:
                    flower[x] = 1
            if check(flower, N, m, k):
                right = day
                res = min(res, day)
            else:
                left = day + 1
        return res
