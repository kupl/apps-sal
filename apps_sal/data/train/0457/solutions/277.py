class Solution:
    IMPOSSIBLE = -1
    
    def computeMinCoins(self, n: int) -> int:
        if n in self.memoization:
            return self.memoization.get(n)
        if n == 0:
            result = 0
        else:
            result = Solution.IMPOSSIBLE
            for coin in self.coins:
                if coin > n:
                    continue
                coins_extra = self.computeMinCoins(n - coin)
                if coins_extra == Solution.IMPOSSIBLE:
                    continue
                plausible_result = 1 + coins_extra
                if result == Solution.IMPOSSIBLE or result > plausible_result:
                    result = plausible_result
        self.memoization[n] = result
        return result
            
    
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        if amount % coins[0] == 0:
            return amount // coins[0]
        self.coins = coins
        self.memoization = {}
        return self.computeMinCoins(amount)

