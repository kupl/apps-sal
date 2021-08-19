class Solution:
    IMPOSSIBLE = -1

    def computeMinCoins(self, n: int) -> int:
        if (result := self.memoization.get(n)) is not None:
            return result
        if n == 0:
            result = 0
        else:
            result = Solution.IMPOSSIBLE
            for coin in self.coins:
                if coin > n:
                    continue
                if (needed_extra := self.computeMinCoins(n - coin)) != Solution.IMPOSSIBLE:
                    possible_result = 1 + needed_extra
                    if result == Solution.IMPOSSIBLE or result > possible_result:
                        result = possible_result
        self.memoization[n] = result
        return result

    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        if amount % coins[0] == 0:
            return amount // coins[0]
        self.coins = coins
        self.memoization = {}
        return self.computeMinCoins(amount)
