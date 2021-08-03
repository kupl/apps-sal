class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        d = {}
        ans = self.helper(coins, amount, d)
        if ans == 100000000:
            return -1
        return ans

    def helper(self, coins, amount, d):
        if amount == 0:
            return 0
        ans = 100000000
        for i in range(len(coins) - 1, -1, -1):
            if coins[i] <= amount:
                if amount - coins[i] in d:
                    sub_ans = d[amount - coins[i]]
                else:
                    sub_ans = 1 + self.helper(coins, amount - coins[i], d)
                    d[amount - coins[i]] = sub_ans
                ans = min(ans, sub_ans)
        return ans
