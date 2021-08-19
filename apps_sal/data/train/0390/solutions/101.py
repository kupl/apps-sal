class Solution:

    def winnerSquareGame(self, n: int) -> bool:
        self.memo = dict()
        return self.dfs(n)

    def dfs(self, left):
        if left <= 0:
            return False
        if left in self.memo:
            return self.memo[left]
        squareRoot = int(left ** 0.5)
        res = False
        for i in reversed(list(range(1, squareRoot + 1))):
            if not self.dfs(left - i * i):
                res = True
                break
        self.memo[left] = res
        return res
