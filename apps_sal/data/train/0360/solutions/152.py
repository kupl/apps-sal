class Solution:

    def shipWithinDays(self, weights: List[int], D: int) -> int:
        (l, r) = (max(weights), sum(weights))

        def isPossible(capacity):
            days = 0
            temp = 0
            for w in weights:
                if temp + w <= capacity:
                    temp += w
                else:
                    days += 1
                    temp = w
            return days + 1 <= D
        while l < r:
            mid = l + (r - l) // 2
            if isPossible(mid):
                r = mid
            else:
                l = mid + 1
        return l
