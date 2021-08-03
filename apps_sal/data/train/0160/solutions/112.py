class Solution:
    def dp(self, i, j):
        if (i, j) in self.memo:
            return self.memo[(i, j)]
        if i > j:
            return (0, 0)

        firstTakeLeft, firstTakeRight = self.piles[i] + self.dp(i + 1, j)[1], self.piles[j] + self.dp(i, j - 1)[1]
        if firstTakeLeft > firstTakeRight:
            self.memo[(i, j)] = (firstTakeLeft, self.dp(i + 1, j)[0])
        else:
            self.memo[(i, j)] = (firstTakeRight, self.dp(i, j - 1)[0])

        return self.memo[(i, j)]

    def stoneGame(self, piles: List[int]) -> bool:
        self.piles = piles
        self.memo = {}

        for i in range(len(piles)):
            self.memo[(i, i)] = (piles[i], 0)

        fir, sec = self.dp(0, len(piles) - 1)

        return fir >= sec
