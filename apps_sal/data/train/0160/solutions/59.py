class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        memo = {}

        def find(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if j - i == 1:
                return max(piles[i], piles[j])
            memo[(i, j)] = max(min(find(i + 1, j - 1), find(i + 2, j)) + piles[i], min(find(i + 1, j - 1), find(i, j - 2)) + piles[j])
            return memo[(i, j)]
        return find(0, len(piles) - 1) > sum(piles) // 2
