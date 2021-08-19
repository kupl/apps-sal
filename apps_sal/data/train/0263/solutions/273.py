class Solution:

    def knightDialer(self, N: int) -> int:
        memo = {}
        moves = [[4, 6], [6, 8], [7, 9], [4, 8], [3, 9, 0], [], [1, 7, 0], [2, 6], [1, 3], [2, 4]]
        for i in range(0, 10):
            memo[i, 0] = 0
            memo[i, 1] = 1
        for n in range(2, N + 1):
            for i in range(0, 10):
                memo[i, n] = 0
                for nextDig in moves[i]:
                    memo[i, n] += memo[nextDig, n - 1]
        total = 0
        for i in range(0, 10):
            total += memo[i, N]
        return total % (10 ** 9 + 7)
