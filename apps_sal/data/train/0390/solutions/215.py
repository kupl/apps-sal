class Solution:

    def winnerSquareGame(self, n: int) -> bool:
        win = [False] * (n + 1)
        for i in range(n):
            if not win[i]:
                j = 1
                while i + j ** 2 <= n:
                    if i + j ** 2 == n:
                        return True
                    win[i + j ** 2] = True
                    j += 1
        return False
