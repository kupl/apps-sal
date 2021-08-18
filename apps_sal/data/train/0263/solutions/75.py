class Solution:
    def knightDialer(self, N: int) -> int:

        moves = {1: {6, 8}, 2: {9, 7}, 3: {8, 4}, 4: {3, 9, 0}, 5: {}, 6: {1, 7, 0}, 7: {2, 6}, 8: {1, 3}, 9: {2, 4}, 0: {4, 6}}
        dp = [1] * 10

        for i in range(2, N + 1):
            newDp = [0] * 10
            for j in range(10):
                for conn in moves[j]:
                    newDp[conn] += dp[j] % (10**9 + 7)

            dp = newDp

        print(dp)
        return sum(dp) % (10**9 + 7)
