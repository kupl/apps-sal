class Solution:

    def shipWithinDays(self, weights: List[int], D: int) -> int:
        (l, r) = (max(weights), sum(weights))
        while l < r:
            mid = (l + r) // 2
            d = self.check(weights, mid)
            if d > D:
                (l, r) = (mid + 1, r)
            else:
                (l, r) = (l, mid)
        return l

    def check(self, weights, size):
        c = 0
        i = 0
        days = 0
        while True:
            if i == len(weights):
                break
            while i < len(weights) and c + weights[i] <= size:
                c += weights[i]
                i += 1
            c = 0
            days += 1
        return days
