class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        # Approach: dfs with memoization - O(nn**0.5)
        self.memo = dict()
        return self.dfs(n)

    def dfs(self, stonesRemain):
        if stonesRemain <= 0:
            return False

        if stonesRemain in self.memo:
            return self.memo[stonesRemain]

        squareRoot = int(stonesRemain ** 0.5)
        res = False

        # iterate from the largest square
        for i in reversed(range(1, squareRoot + 1)):
            posRes = self.dfs(stonesRemain - i * i)
            # if there's a way such that opponent loses, we know
            # that we can win with current number of stones
            # So, we terminate early
            if not posRes:
                res = True
                break

        self.memo[stonesRemain] = res
        return res
