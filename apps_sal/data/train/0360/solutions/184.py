class Solution:

    def shipWithinDays(self, weights: List[int], D: int) -> int:
        l = max(weights)
        r = sum(weights)
        length = len(weights)
        while l <= r:
            mid = l + (r - l) // 2
            cur = 0
            toD = 1
            for i in range(length):
                if cur + weights[i] > mid:
                    toD += 1
                    cur = 0
                cur += weights[i]
            if toD > D:
                l = mid + 1
            else:
                r = mid - 1
        return l
