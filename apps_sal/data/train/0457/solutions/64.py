class Solution:

    def do_du_tab(self, coins, amount):
        dp_tab = [math.inf for _ in range(amount + 1)]
        dp_tab[0] = 0
        for a in range(1, amount + 1):
            potential = []

            for coin in coins:
                potential.append(dp_tab[a - coin] + 1)

            dp_tab[a] = min(potential)

        return dp_tab[-1] if dp_tab[-1] != float('inf') else -1

    def do_something(self, coins, amount):
        dp_tab = [math.inf for _ in range(amount + 1)]
        dp_tab[0] = 0

        for i in range(1, amount + 1):
            temp = []
            for coin in coins:
                temp.append(dp_tab[i - coin])

            dp_tab[i] = min(temp) + 1
        return dp_tab[amount] if dp_tab[amount] != float('inf') else -1

    def coinChange(self, coins: List[int], amount: int) -> int:

        if len(coins) == 0:
            return 0
        if amount == 0:
            return 0

        c = [coin for coin in coins if coin <= amount]
        if len(c) == 0:
            return -1
        # c.sort(reverse=True)
        return self.do_something(c, amount)
        # return self.do_du_tab(c, amount)
