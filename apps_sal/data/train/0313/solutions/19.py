class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        def isPossible(t):
            count = 0
            res = 0
            for i in range(len(bloomDay)):
                if bloomDay[i] <= t:
                    count += 1
                    if count == k:
                        count = 0
                        res += 1
                else:
                    count = 0
            return res >= m

        s, e = 0, max(bloomDay) + 1

        while s < e:
            mid = (s + e) // 2
            if isPossible(mid):
                e = mid
            else:
                s = mid + 1

        if s == max(bloomDay) + 1:
            return -1

        return s
