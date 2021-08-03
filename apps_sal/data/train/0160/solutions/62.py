class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        def dp(m, n, x):
            if m > n:
                return 0
            if t[m][n] != -1:
                return t[m][n]
            else:
                if x == 0:
                    self.cost1 += max((dp(m + 1, n, 1) + piles[m]), dp(m, n - 1, 1) + piles[n])
                    t[m][n] = self.cost1
                    return t[m][n]
                else:
                    self.cost2 += max((dp(m + 1, n, 0) + piles[m]), dp(m, n - 1, 0) + piles[n])
                    t[m][n] = self.cost2
                    return t[m][n]
        self.cost1 = 0
        n = len(piles)
        self.cost2 = 0
        t = [[-1] * (n + 1) for i in range(n + 1)]
        dp(0, n - 1, 0)
        print((self.cost1, self.cost2))
        if self.cost1 > self.cost2:
            return True
        else:
            return False
