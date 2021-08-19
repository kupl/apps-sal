class Solution:

    def knightDialer(self, n: int) -> int:
        KMOD = 10 ** 9 + 7
        moves = [[4, 6], [8, 6], [7, 9], [4, 8], [3, 9, 0], [], [1, 7, 0], [2, 6], [1, 3], [2, 4]]
        dp = [1 for _ in range(10)]
        for k in range(1, n):
            cur = [0 for _ in range(10)]
            for i in range(10):
                for from_key in moves[i]:
                    cur[from_key] += dp[i]
            dp = cur
        result = 0
        for i in range(10):
            result += dp[i]
        return result % KMOD
