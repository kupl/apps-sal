class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        # time complexity: O(N*logN)
        # space complexity: O(N)
        dp = [False]
        for i in range(1, n + 1):
            s = False
            for j in range(1, int(i ** 0.5) + 1):
                if not dp[i - j ** 2]:
                    s = True
                    break
            dp.append(s)
        return dp[-1]
