class Solution:

    def shipWithinDays(self, weights: List[int], D: int) -> int:

        def numberofDaysWithCapacity(weights, mid):
            (sum, c) = (0, 1)
            for i in range(len(weights)):
                sum += weights[i]
                if sum > mid:
                    c += 1
                    sum = weights[i]
            return c
        (left, right) = (max(weights), sum(weights))
        while left <= right:
            mid = left + (right - left) // 2
            daysRequired = numberofDaysWithCapacity(weights, mid)
            if daysRequired > D:
                left = mid + 1
            else:
                res = mid
                right = mid - 1
        return res
