class Solution:

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        def condition(x):
            bloom = [0] * len(bloomDay)
            for (i, day) in enumerate(bloomDay):
                if day <= x:
                    bloom[i] = 1
            count = 0
            M = 0
            for flower in bloom:
                if flower:
                    count += 1
                else:
                    count = 0
                if count >= k:
                    count = 0
                    M += 1
                if M >= m:
                    return True
            return False
        if len(bloomDay) < m * k:
            return -1
        left = min(bloomDay)
        right = max(bloomDay)
        while left < right:
            mid = left + (right - left) // 2
            if condition(mid):
                right = mid
            else:
                left = mid + 1
        return left
