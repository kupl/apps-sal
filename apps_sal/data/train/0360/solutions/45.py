class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        l = max(weights)
        r = 10**9

        while l < r:
            m = l + (r - l) // 2
            # now check if we use this m as the weight capacity for ship how many days we need
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
