class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:

        def good(d):
            c, prev = 1, 0
            for i in range(1, len(position)):
                if position[i] - position[prev] >= d:
                    c += 1
                    prev = i

                if c == 0:
                    break

            return c

        position.sort()
        l, r = 0, position[-1] - position[0]

        while l <= r:
            mid = (r + l) // 2

            if good(mid) >= m:
                l = mid + 1

            else:
                r = mid - 1

        return r
