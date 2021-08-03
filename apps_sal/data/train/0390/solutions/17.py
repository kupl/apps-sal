class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        squares = [i**2 for i in range(1, int(sqrt(n)) + 1)]
        A = [False for _ in range(n + 1)]

        for i in range(1, n + 1):
            if i in squares:
                A[i] = True
                continue

            for square in squares:
                if square > i:
                    break

                if not A[i - square]:
                    A[i] = True
                    break

        return A[n]
