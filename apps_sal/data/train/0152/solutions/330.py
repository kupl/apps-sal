class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        def can_reach(force):
            last = position[0]
            placed = 1

            for i in range(1, len(position)):
                pos = position[i]

                if pos - last >= force:
                    last = pos
                    placed += 1
                if placed >= m:
                    break

            return placed >= m

        l = 1
        r = position[-1] - position[0] + 1

        while l < r:
            mid = (l + r) // 2
            if not can_reach(mid):
                r = mid
            else:
                l = mid + 1

        return l - 1
