class Solution:
    def maxDistance(self, pos: List[int], m: int) -> int:

        pos.sort()

        low = 0

        high = pos[-1] - pos[0]

        def chk(d):

            nonlocal m

            n = len(pos)

            c = m
            p = 0

            for i in range(n):

                if c == 0:
                    return True

                if i == 0:
                    c -= 1
                    p = pos[0]
                    continue

                if pos[i] - p >= d:
                    c -= 1
                    p = pos[i]

            return c <= 0

        while low < high:

            mid = int(math.ceil((low + high) / 2))

            if chk(mid):
                low = mid
            else:
                high = mid - 1

        return low
