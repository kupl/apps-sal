class Solution:

    def shipWithinDays(self, weights: List[int], D: int) -> int:

        def test(x):
            (times, i) = (0, 0)
            while i < len(weights):
                times += 1
                cur = 0
                while i < len(weights) and cur + weights[i] <= x:
                    cur += weights[i]
                    i += 1
            return times
        (l, r) = (max(weights), sum(weights))
        while l <= r:
            mid = (l + r) // 2
            days = test(mid)
            if days <= D:
                r = mid - 1
            else:
                l = mid + 1
        if days > D:
            mid += 1
        return mid
