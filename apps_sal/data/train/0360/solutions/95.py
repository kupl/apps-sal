class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        s = max(weights)
        e = max(weights) * len(weights) // D

        def dayCount(weights, cap, D):
            day = 1
            total = 0
            for i in range(len(weights)):
                if total + weights[i] <= cap:
                    total += weights[i]
                else:
                    day += 1
                    total = weights[i]
            return day <= D

        while s <= e:
            mid = (s + e) // 2
            if dayCount(weights, mid, D):
                e = mid - 1
            else:
                s = mid + 1
        return s
