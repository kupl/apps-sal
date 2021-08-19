class Solution:

    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        def check(mid):
            curr = position[0]
            placed = 1
            for i in range(len(position)):
                if position[i] >= curr + mid:
                    placed += 1
                    curr = position[i]
            return placed >= m
        (l, r) = (1, 10 ** 9 + 1)
        while l < r:
            mid = (l + r + 1) // 2
            if check(mid):
                l = mid
            else:
                r = mid - 1
        return l
