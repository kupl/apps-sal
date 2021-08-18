class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        return self.dfs(coins, 0, 0, amount, -1)

    def dfs(self, coins: List[int], idx: int, cnt: int, amount: int, minCnt: int) -> int:
        if amount == 0:
            return cnt
        if idx >= len(coins):
            return -1

        if minCnt > 0 and cnt + amount // coins[idx] + 1 > minCnt:
            return -1

        for i in range(amount // coins[idx], -1, -1):
            res = self.dfs(coins, idx + 1, cnt + i, amount - coins[idx] * i, minCnt)
            if res != -1:
                minCnt = res if minCnt == -1 else min(minCnt, res)
        return minCnt
