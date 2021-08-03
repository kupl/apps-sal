class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        left = int(sum(weights) / D)
        right = max(weights) * len(weights) / D

        def is_valid(weights, D, capacity):
            cur = capacity
            day = 0
            for w in weights:
                if cur + w <= capacity:
                    cur += w
                else:
                    cur = 0
                    if capacity < w:
                        return False
                    else:
                        cur = w
                        day += 1
            if day <= D:
                return True
            return False

        while left <= right:
            mid = left + (right - left) // 2
            if is_valid(weights, D, mid):
                right = mid - 1
            else:
                left = mid + 1
        return int(left)
