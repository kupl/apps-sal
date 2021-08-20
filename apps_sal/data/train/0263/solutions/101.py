class Solution:

    def knightDialer(self, n: int) -> int:
        validJumps = [[4, 6], [6, 8], [7, 9], [4, 8], [3, 9, 0], [], [1, 7, 0], [2, 6], [1, 3], [2, 4]]
        memo = [[0 for _ in range(n + 1)] for _ in range(10)]
        for i in range(len(memo)):
            memo[i][1] = 1
        for j in range(2, n + 1):
            for i in range(len(memo)):
                for k in validJumps[i]:
                    memo[i][j] = (memo[i][j] + memo[k][j - 1]) % (10 ** 9 + 7)
        ans = 0
        for i in range(10):
            ans = (ans + memo[i][n]) % (10 ** 9 + 7)
        return ans
