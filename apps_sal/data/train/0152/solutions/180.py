class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        def guess(position, m, guess):
            placed = 1
            last = position[0]
            i = 1
            while i < len(position):
                if position[i] - last >= guess:
                    placed += 1
                    last = position[i]

                if placed == m:
                    return True

                i += 1

            return placed >= m

        position.sort()
        l = 0
        r = position[-1] - position[0]
        while l < r:
            mid = (l + r + 1) // 2
            if guess(position, m, mid):
                l = mid
            else:
                r = mid - 1

        return l
