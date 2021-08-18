class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        ways = [[0] * min(251, arrLen) for _ in range(steps + 1)]
        ways[0][0] = 1
        for k in range(1, steps + 1):
            for i in range(len(ways[k])):
                for offset in [-1, 0, 1]:
                    if 0 <= i + offset < len(ways[k]):
                        ways[k][i] += ways[k - 1][i + offset]
                ways[k][i] %= 10**9 + 7
        return ways[-1][0]
