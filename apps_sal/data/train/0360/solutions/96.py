class Solution:

    def shipWithinDays(self, weights: List[int], D: int) -> int:
        left = max(weights)
        right = 999999999999999999
        while left < right:
            mid = (left + right) // 2
            days_needed = 1
            cargo = 0
            for w in weights:
                if cargo + w > mid:
                    days_needed += 1
                    cargo = w
                else:
                    cargo += w
            if days_needed > D:
                left = mid + 1
            else:
                right = mid
        return left
