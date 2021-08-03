class Solution:
    def knightDialer(self, n: int) -> int:
        moves = [[4, 6], [6, 8], [7, 9], [4, 8], [0, 3, 9], [], [1, 7, 0], [2, 6], [1, 3], [2, 4]]

        dp = [1] * 10
        for _ in range(n - 1):
            dp2 = [0] * 10
            for i in range(10):
                dp2[i] = sum(dp[j] for j in moves[i]) % (10**9 + 7)

            dp = dp2

        return sum(dp) % (10**9 + 7)

    # def knightDialer(self, N: int) -> int:
    #     pad, cnt = [[4, 6], [6, 8], [7, 9], [4, 8], [0, 3, 9], [], [0, 1, 7], [2, 6], [1, 3], [2, 4]], [1]*10
    #     for _ in range(N-1):
    #         next_cnt = [1]*10
    #         for i in range(10):
    #             next_cnt[i] = sum(cnt[j] for j in pad[i]) % (10**9+7)
    #         cnt = next_cnt
    #     return sum(cnt) % (10**9+7)
