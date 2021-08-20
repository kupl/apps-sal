"""
use DP instead of BFS, becasue only finite many states
2D DP:
DP[l][s] = number of unique path of length l, starting with state s
DP[l][1] = DP[l-1][6] + DP[l-1][8], becasue 1 can move to 6, 8
"""


class Solution:

    def knightDialer(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        movedict = {0: [4, 6], 1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [3, 9, 0], 5: [], 6: [1, 7, 0], 7: [2, 6], 8: [1, 3], 9: [2, 4]}
        DP = [[0] * 10 for _ in range(n)]
        DP[0] = [1] * 10
        for l in range(1, n):
            for s in range(10):
                for moveto in movedict[s]:
                    DP[l][s] += DP[l - 1][moveto]
                    DP[l][s] %= MOD
        ans = sum(DP[-1]) % MOD
        return ans
