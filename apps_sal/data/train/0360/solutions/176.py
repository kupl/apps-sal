class Solution:

    def shipWithinDays(self, weights: List[int], D: int) -> int:

        def feasible(capacity):
            days = 1
            total = 0
            for i in range(len(weights)):
                total += weights[i]
                if total > capacity:
                    days += 1
                    total = weights[i]
                if days > D:
                    return False
            return True
        (left, right) = (max(weights), sum(weights))
        while left < right:
            mid = left + (right - left) // 2
            if feasible(mid):
                right = mid
            else:
                left = mid + 1
        return left
