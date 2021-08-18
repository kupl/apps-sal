class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1

        def feasible(day):
            banquet = 0
            streak = 0
            for d in bloomDay:
                if d > day:
                    streak = 0
                else:
                    streak += 1
                    if streak == k:
                        banquet += 1
                        streak = 0
                    if banquet == m:
                        return True
            return False

        low, high = min(bloomDay), max(bloomDay)
        while low < high:
            mid = (low + high) // 2
            if feasible(mid):
                high = mid
            else:
                low = mid + 1
        return low
