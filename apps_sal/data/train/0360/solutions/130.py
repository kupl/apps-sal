class Solution:

    def shipWithinDays(self, weights: List[int], D: int) -> int:

        def check(capacity):
            cur = ix = 0
            day = 1
            while ix < len(weights):
                if cur + weights[ix] == capacity:
                    cur = 0
                    day += 1
                elif cur + weights[ix] > capacity:
                    cur = weights[ix]
                    day += 1
                else:
                    cur += weights[ix]
                ix += 1
            return ix == len(weights) and day <= D
        (left, right) = (max(weights), sum(weights))
        while left < right:
            mid = left + (right - left) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left
