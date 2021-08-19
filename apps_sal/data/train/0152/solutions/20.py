class Solution:

    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        l = 0
        r = (position[-1] - 1) // (m - 1) * 2
        while l < r:
            intrv = (l + r) // 2
            c = 0
            prev = float('-inf')
            for p in position:
                if p >= prev + intrv:
                    c += 1
                    prev = p
            if c >= m:
                best = intrv
                l = intrv + 1
            else:
                r = intrv
        return best
