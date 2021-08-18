class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        def feasible(d) -> bool:
            count = 0
            prevBadIndex = -1
            for i in range(len(bloomDay)):
                if bloomDay[i] > d:
                    count += (i - prevBadIndex - 1) // k
                    prevBadIndex = i

            if prevBadIndex != len(bloomDay) - 1:
                count += (len(bloomDay) - prevBadIndex - 1) // k

            return count >= m

        if len(bloomDay) < (m * k):
            return -1

        left, right = min(bloomDay), max(bloomDay)

        while left < right:
            mid = left + (right - left) // 2

            if feasible(mid):
                right = mid
            else:
                left = mid + 1

        return left
