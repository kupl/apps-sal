class Solution:
    def checkDate(self, bloom, m, k, day):
        streak = 0
        count = 0
        for b in bloom:
            if b <= day:
                streak += 1
                if streak == k:
                    count += 1
                    if count == m:
                        return True
                    streak = 0
            else:
                streak = 0
        return False

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        left, right = min(bloomDay), max(bloomDay) + 1

        while left < right:
            mid = left + (right - left) // 2
            if self.checkDate(bloomDay, m, k, mid):
                right = mid
            else:
                left = mid + 1

        return left if left != max(bloomDay) + 1 else -1
