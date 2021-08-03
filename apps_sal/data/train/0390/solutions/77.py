class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        ans = [False] * (n + 1)
        for i in range(1, n + 1):
            ans[i] = not all(ans[i - j**2] for j in range(1, 1 + int(i**.5)))
        return ans[-1]
