class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        INVALID = 10 ** 10
        self.ans = INVALID

        def dfs(s, amount, count):
            if amount == 0:
                self.ans = count
                return
            if s == len(coins):
                return
            coin = coins[s]
            for i in range(amount // coin, -1, -1):
                print(i)
                print(coin)
                print(amount)
                if count + i >= self.ans:
                    break
                dfs(s + 1, amount - i * coin, count + i)
        dfs(0, amount, 0)
        if self.ans == INVALID:
            return -1
        else:
            return self.ans
