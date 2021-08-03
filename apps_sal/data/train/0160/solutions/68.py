class Solution:

    def stoneGame(self, piles: List[int]) -> bool:

        self.piles = piles
        self.dp = {}

        def helper(i, j, turn=True):

            if i > j:
                return 0
            if (i, j) in self.dp:
                return self.dp[(i, j)]
            alex = 0
            if turn:
                alex = max(self.piles[i] + helper(i + 1, j, turn=False), self.piles[j] + helper(i, j - 1, turn=False))
            else:
                alex = max(helper(i + 1, j, turn=True), helper(i, j - 1, turn=True))

            self.dp[(i, j)] = alex
            return self.dp[(i, j)]

        alex = helper(0, len(self.piles) - 1)
        return 2 * alex > sum(self.piles)
