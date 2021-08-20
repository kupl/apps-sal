class Solution:

    def maxDistance(self, position: List[int], m: int) -> int:
        n = len(position)
        position.sort()

        def count(d):
            (ans, curr) = (1, position[0])
            for x in position[1:]:
                if x - curr >= d:
                    (ans, curr) = (ans + 1, x)
            return ans
        (l, r) = (1, position[-1] - position[0] + 1)
        while l < r:
            p = l + (r - l) // 2
            if count(p) >= m:
                l = p + 1
            else:
                r = p
        return l - 1
