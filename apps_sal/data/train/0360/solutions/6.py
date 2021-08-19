class Solution:

    def shipWithinDays(self, weights: List[int], D: int) -> int:
        left = max(weights)
        right = sum(weights)
        while left <= right:
            (mid, days_needed, cur) = (int((left + right) / 2), 1, 0)
            for w in weights:
                if cur + w > mid:
                    days_needed += 1
                    cur = 0
                cur += w
            if days_needed > D:
                left = mid + 1
            else:
                right = mid - 1
        return left
