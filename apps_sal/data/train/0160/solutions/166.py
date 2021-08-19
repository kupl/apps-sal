class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # use dp
        # answer the question \"what is the expected gain of the current player over the next player given the plies[i : j] (inclusive)\"
        table = [[0 for _ in range(len(piles))] for _ in range(len(piles))]

        # base case - single element
        for i in range(len(piles)):
            table[i][i] = piles[i]

        for diff in range(1, len(piles)):
            for i in range(0, len(piles) - diff):
                table[i][i + diff] = max(piles[i] - table[i + 1][i + diff],
                                         piles[i + diff] - table[i][i + diff - 1])

        return table[0][len(piles) - 1] > 0
