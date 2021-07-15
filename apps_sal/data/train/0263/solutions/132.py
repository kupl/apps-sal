class Solution:
    def knightDialer(self, n: int) -> int:
        moves = [[4, 6], [6, 8], [9, 7], [8, 4], [3, 9, 0], [], [7, 1, 0], [6, 2], [1, 3], [2, 4]]
        count = [[0] * 10 for _ in range(n + 1)]
        for i in range(10):
            count[1][i] = 1
        for i in range(1, n + 1):
            for num in range(10):
                for nei in moves[num]:
                    count[i][num] += count[i - 1][nei]
                    count[i][num] %= 10 ** 9 + 7
        return sum(count[-1]) % (10 ** 9 + 7)
