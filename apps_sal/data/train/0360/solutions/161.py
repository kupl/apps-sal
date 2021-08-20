class Solution:

    def shipWithinDays(self, weights: List[int], D: int) -> int:
        left = max(weights)
        right = sum(weights)
        res = right
        while left <= right:
            mid = left + (right - left) // 2
            d = self.get_day(weights, mid)
            if d <= D:
                res = min(res, mid)
                right = mid - 1
            else:
                left = mid + 1
        return res

    def get_day(self, weights, cap):
        cur = 0
        res = 0
        for x in weights:
            if cur + x > cap:
                res += 1
                cur = 0
            cur += x
        return res + 1
