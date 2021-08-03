class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        l, r = max(weights), sum(weights)
        while(l < r):
            m, n, c = (l + r) / 2, 1, 0
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
        '''left, right = max(weights), sum(weights)
        while left < right:
            mid, need, cur = (left + right) / 2, 1, 0
            for w in weights:
                if cur + w > mid:
                    need += 1
                    cur = 0
                cur += w
            if need > D: left = mid + 1
            else: right = mid
        return left'''
