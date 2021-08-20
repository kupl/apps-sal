class Solution:

    def winnerSquareGame(self, n: int) -> bool:
        self.memo = dict()
        return self.dfs(n)

    def dfs(self, stonesRemain):
        if stonesRemain <= 0:
            return False
        if stonesRemain in self.memo:
            return self.memo[stonesRemain]
        squareRoot = int(stonesRemain ** 0.5)
        res = False
        for i in reversed(range(1, squareRoot + 1)):
            if not self.dfs(stonesRemain - i * i):
                res = True
                break
        self.memo[stonesRemain] = res
        return res
