class Solution:

    def shipWithinDays(self, weights: List[int], D: int) -> int:
        l = max(weights)
        r = 10 ** 9
        while l < r:
            m = l + (r - l) // 2
            days = 1
            s = 0
            for i in range(len(weights)):
                if s + weights[i] > m:
                    days += 1
                    s = weights[i]
                else:
                    s += weights[i]
            if days <= D:
                r = m
            else:
                l = m + 1
        return l
