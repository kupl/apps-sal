class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        dp = [[
              0
              for egg in range(K + 1)]
              for moves in range(305)]
        print(N)

        for move in range(1, 300):
            for eggs in range(1, K + 1):
                dp[move][eggs] = 1 + dp[move - 1][eggs - 1] + dp[move - 1][eggs]
                if dp[move][eggs] >= N:
                    return move
