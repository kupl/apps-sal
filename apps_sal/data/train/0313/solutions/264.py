class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1

        def feasible(days, m, k):
            flowers = 0
            bouq = 0
            for item in bloomDay:
                if item <= days:
                    flowers += 1
                else:
                    flowers = 0
                if flowers >= k:
                    bouq += 1
                    flowers = 0
                    if bouq == m:
                        return True
            return False

        left = min(bloomDay)
        right = max(bloomDay)
        while left < right:
            mid = left + (right - left) // 2
            if feasible(mid, m, k):
                right = mid
            else:
                left = mid + 1
        return left
