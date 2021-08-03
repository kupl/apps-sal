class Solution:
    def check(self, weights, limit):
        cur = 0
        count = 1
        for i in range(len(weights)):
            if cur + weights[i] > limit:
                count += 1
                cur = weights[i]
            else:
                cur += weights[i]

        return count

    def shipWithinDays(self, weights: List[int], D: int) -> int:
        l = max(weights)
        r = sum(weights)
        ans = 1

        while l <= r:
            mid = l + int((r - l) / 2)
            if self.check(weights, mid) <= D:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans
