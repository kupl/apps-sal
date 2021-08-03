class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        n = len(position)

        # count number of balls that can be put in basket with min_force d
        def count(d):
            ans, curr = 1, position[0]
            for i in range(1, n):
                if position[i] - curr >= d:
                    ans += 1
                    curr = position[i]
            return ans

        l, r = 1, position[-1] - position[0]
        while l < r:
            f = r - (r - l) // 2  # l + (r - l) // 2
            if count(f) >= m:
                l = f
            else:
                r = f - 1

        return l
