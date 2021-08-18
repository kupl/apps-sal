class Solution:

    def do_du_tab(self, coins, amount):
        dp_tab = [math.inf for _ in range(amount + 1)]
        dp_tab[0] = 0
        for i in range(len(coins)):
            for a in range(1, amount + 1):
                if a >= coins[i]:
                    dp_tab[a] = min(dp_tab[a], 1 + dp_tab[a - coins[i]])
        return dp_tab[amount]

    def do_td_mem(self, cache, coins, amount, index):

        if amount == 0:
            return 0

        if len(coins) <= index:
            return math.inf

        if cache[index][amount] == math.inf:
            count_keeping_element = math.inf
            if coins[index] <= amount:
                temp = self.do_td_mem(cache, coins, amount - coins[index], index)
                if temp != math.inf:
                    count_keeping_element = temp + 1

            count_skipping_element = self.do_td_mem(cache, coins, amount, index + 1)
            cache[index][amount] = min(count_keeping_element, count_skipping_element)
        return cache[index][amount]

    def do_bf(self, coins, amount, index):
        if amount == 0:
            return 0
        n = len(coins)
        if n <= index:
            return math.inf

        count_keeping_element = math.inf
        if coins[index] <= amount:
            temp = self.do_bf(coins, amount - coins[index], index)
            if temp != math.inf:
                count_keeping_element = temp + 1

        count_skipping_element = self.do_bf(coins, amount, index + 1)
        return min(count_keeping_element, count_skipping_element)

    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount < 1:
            return 0
        coins.sort()
        output = self.do_du_tab(coins, amount)
        return -1 if output == math.inf else output
