class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        def helper(c):
            s = 0
            d = 1
            for w in weights:
                s += w
                if s > c:
                    d += 1
                    s = w
                    if d > D:
                        return False
            return True
        l = max(weights)
        r = sum(weights)
        while l < r:
            m = l + (r - l) // 2
            if helper(m):
                r = m
            else:
                l = m + 1
        return l
