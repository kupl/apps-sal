class Solution:
    def winnerSquareGame(self, n: int) -> bool:

        def getSquareNumbers(n: int) -> List[int]:
            return [index * index for index in range(1, 1 + math.floor(math.sqrt(n)))]

        table = [False] * (n + 1)

        for index in range(n + 1):
            table[index] = any(not table[index - lose] for lose in getSquareNumbers(index))

        return table[-1]
