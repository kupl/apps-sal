class Solution:

    def shipWithinDays(self, weights: List[int], D: int) -> int:
        (l, r) = (max(weights), sum(weights))
        while l < r:
            (m, n, c) = ((l + r) / 2, 1, 0)
            for z in weights:
                if c + z > m:
                    n += 1
                    c = 0
                c += z
            if n > D:
                l = m + 1
            else:
                r = m
        return int(l)
        'left, right = max(weights), sum(weights)\n        while left < right:\n            mid, need, cur = (left + right) / 2, 1, 0\n            for w in weights:\n                if cur + w > mid:\n                    need += 1\n                    cur = 0\n                cur += w\n            if need > D: left = mid + 1\n            else: right = mid\n        return left'
