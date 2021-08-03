class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        memo = {}

        def subseq(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i > j:
                return 0
            if (j - i - len(piles)) % 2:
                memo[(i, j)] = max(piles[i] + subseq(i + 1, j), piles[j] + subseq(i, j - 1))
            else:
                memo[(i, j)] = min(-piles[i] + subseq(i + 1, j), -piles[j] + subseq(i, j - 1))
            return memo[(i, j)]
        return subseq(0, len(piles) - 1) > 0
