class Solution:

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

        if 0 in lookup:
            return lookup[0]
        else:
            return -1
