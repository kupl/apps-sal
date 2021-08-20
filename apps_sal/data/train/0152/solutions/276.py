class Solution:

    def maxDistance(self, position: List[int], cuts: int) -> int:
        position = sorted(position)
        (l, r) = (1, position[-1] - position[0])
        while l != r:
            m = (l + r) // 2 + 1
            if self.isValid(position, m, cuts):
                l = m
            else:
                r = m - 1
        return l

    def isValid(self, position, force, cuts):
        c = 0
        l = 0
        for r in range(1, len(position)):
            if position[r] - position[l] >= force:
                c += 1
                l = r
        return c >= cuts - 1
