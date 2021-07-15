class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        def countDays(weights, capacity):
            l, r, cnt, sumv = 0, 0, 0, 0
            while r < len(weights):
                sumv += weights[r]
                if sumv > capacity:
                    cnt += 1
                    l = r
                    sumv = 0
                else:
                    r += 1
            if sumv:
                cnt += 1
            return cnt
        maxv, sumv = max(weights), sum(weights)
        left, right = maxv, sumv
        while left < right:
            mid = (left + right) // 2
            days = countDays(weights, mid)
            if days > D:
                left = mid + 1
            else:
                right = mid
        return left
