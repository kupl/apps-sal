class Solution:

    def knightDialer(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        moves = [[4, 6], [6, 8], [7, 9], [4, 8], [3, 9, 0], [], [1, 7, 0], [2, 6], [1, 3], [2, 4]]
        dp = [[None] * 10 for _ in range(n)]
        for i in range(10):
            dp[0][i] = 1

        def helper(node, jumpsLeft):
            if dp[jumpsLeft][node]:
                return dp[jumpsLeft][node]
            cnt = 0
            for nextJump in moves[node]:
                cnt += helper(nextJump, jumpsLeft - 1)
                cnt %= MOD
            dp[jumpsLeft][node] = cnt
            return cnt
        for i in range(10):
            helper(i, n - 1)
        return sum(dp[n - 1]) % MOD
