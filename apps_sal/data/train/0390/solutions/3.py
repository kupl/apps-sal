class Solution:

    def winnerSquareGame(self, n: int) -> bool:
        table = [False] * (n + 1)
        for index in range(n + 1):
            table[index] = any((not table[index - lose * lose] for lose in range(1, 1 + math.floor(math.sqrt(index)))))
        return table[-1]
