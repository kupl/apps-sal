class Solution:

    def coinChange_bottomUp(self, coins: List[int], amount: int) -> int:
        lookup = {x: amount + 1 for x in range(1, amount + 1)}
        lookup[0] = 0
        for i in range(amount + 1):
            for coin in coins:
                remainder = i - coin
                if remainder < 0:
                    continue
                best_min = min(lookup[remainder] + 1, lookup[i])
                lookup[i] = best_min
        if lookup[i] > amount:
            return -1
        else:
            return lookup[i]

    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        coins.reverse()
        lookup = {}

        def find_combos(total_remain, total_coins):
            if total_remain in lookup:
                if lookup[total_remain] > total_coins:
                    lookup[total_remain] = total_coins
                else:
                    return
            else:
                lookup[total_remain] = total_coins
            for coin in coins:
                if total_remain - coin < 0:
                    continue
                find_combos(total_remain - coin, total_coins + 1)
        find_combos(amount, 0)
        return lookup[0] if 0 in lookup else -1
