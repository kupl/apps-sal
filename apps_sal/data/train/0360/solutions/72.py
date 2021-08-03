class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        def can(K):
            i = 0
            days = 0
            while i < len(weights) and days <= D + 1:
                k = K
                days += 1
                while i < len(weights) and k >= weights[i]:
                    k -= weights[i]
                    i += 1
            return days <= D

        l, r = 1, sum(weights)
        while l < r:
            mid = (l + r) // 2
            if can(mid):
                r = mid
            else:
                l = mid + 1
        return l
