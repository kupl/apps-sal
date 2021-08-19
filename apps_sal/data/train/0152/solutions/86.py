class Solution:

    def nnpossible(self, pos, k, m) -> bool:
        prev = pos[0]
        k -= 1
        for i in pos:
            if i - prev >= m:
                k -= 1
                prev = i
            if k == 0:
                break
        return k == 0

    def maxDistance(self, position: List[int], k: int) -> int:
        position.sort()
        l = 0
        r = position[-1] + 1

        while r - l > 1:
            m = (l + r) // 2
            if self.nnpossible(position, k, m):
                l = m
            else:
                r = m
        return l


# TTTFFF
