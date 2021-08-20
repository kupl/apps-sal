class Solution:

    def shipWithinDays(self, weights: List[int], D: int) -> int:

        def check_capacity(capacity) -> bool:
            days = 1
            ship_weight = 0
            for weight in weights:
                ship_weight += weight
                if ship_weight > capacity:
                    ship_weight = weight
                    days += 1
                    if days > D:
                        return False
            return True
        left = max(weights)
        right = left * len(weights) // D
        while left < right:
            mid = left + (right - left) // 2
            if check_capacity(mid):
                right = mid
            else:
                left = mid + 1
        return left
