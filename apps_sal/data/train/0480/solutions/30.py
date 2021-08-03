class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        # nw(s, idx): number of ways to end up at idx after s steps
        # nw(s, idx) = s * (nw(s - 1, idx) + nw(s - 1, idx - 1) + nw(s - 1, idx + 1))

        nw = [[0 for _ in range(min(arrLen, steps + 1))] for _ in range(steps + 1)]
        nw[0][0] = 1

        # arr  0 1
        #    0 1 0
        #  s 1 1 1
        #    2 2 2
        #    3 4 4

        for s in range(1, steps + 1):
            for idx in range(min(arrLen, steps + 1)):
                ways = nw[s - 1][idx]
                if idx > 0:
                    ways += nw[s - 1][idx - 1]
                if idx < min(arrLen, steps + 1) - 1:
                    ways += nw[s - 1][idx + 1]
                nw[s][idx] = ways

        return nw[steps][0] % (10**9 + 7)
