class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        self.res = float('inf')
        n = len(coins)
        coins.sort(reverse=True)

        def helper(cur, start, cnt, n):
            if cur == amount:
                self.res = min(self.res, cnt)
            if cur > amount:
                return
            for i in range(start, n):
                if cur + coins[i] <= amount and cur + coins[i] * (self.res - cnt) > amount:
                    helper(cur + coins[i], i, cnt + 1, n)
        helper(0, 0, 0, n)
        return self.res if self.res < float('inf') else -1
