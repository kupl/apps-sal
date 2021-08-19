class Solution:

    def maxDistance(self, position, m) -> int:
        position.sort()
        l = 0
        r = position[-1] - position[0]

        def isValid(dist):
            used = 1
            curr = position[0]
            for j in range(1, len(position)):
                if position[j] - curr >= dist:
                    used += 1
                    curr = position[j]
            return used
        while l < r:
            d = r - (r - l) // 2
            used = isValid(d)
            if used >= m:
                l = d
            else:
                r = d - 1
        return r
