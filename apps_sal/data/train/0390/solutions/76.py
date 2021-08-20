class Solution:

    def winnerSquareGame(self, n: int) -> bool:
        sol = [False] * (n + 1)
        for i in range(1, n + 1):
            j = pwr = 1
            sol[i] = False
            while pwr <= i:
                if not sol[i - pwr]:
                    sol[i] = True
                    break
                j += 1
                pwr = j ** 2
        return sol[-1]
