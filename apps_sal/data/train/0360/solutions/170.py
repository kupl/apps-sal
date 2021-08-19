class Solution:

    def shipWithinDays(self, weights, D):
        (l, r) = (max(weights), sum(weights))
        while l < r:
            (m, days, curWeight) = ((l + r) // 2, 1, 0)
            for weight in weights:
                if curWeight + weight > m:
                    days += 1
                    curWeight = 0
                if days > D:
                    l = m + 1
                    break
                curWeight += weight
            else:
                r = m
        return l
