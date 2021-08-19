class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        def binarySearch(capacity):
            days = 1
            total = 0
            for i in weights:
                total += i
                if total > capacity:  # wait for the next day
                    total = i
                    days += 1
                    if days > D:  # cannot ship
                        return False
            return True
        left, right = max(weights), sum(weights)
        while left < right:
            mid = left + (right - left) // 2
            if binarySearch(mid):
                right = mid
            else:
                left = mid + 1
        return left
