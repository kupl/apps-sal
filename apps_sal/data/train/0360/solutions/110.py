class Solution:

    def shipWithinDays(self, weights: List[int], D: int) -> int:
        (l, r) = (max(weights), sum(weights))
        while l <= r:
            mid = l + (r - l) // 2
            (need, cur) = (1, 0)
            for w in weights:
                if cur + w > mid:
                    need += 1
                    cur = 0
                cur += w
            if need > D:
                l = mid + 1
            else:
                r = mid - 1
        return l
