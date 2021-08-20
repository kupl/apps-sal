class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:

        def make_change(sum_remaining, coins, mem):
            if sum_remaining < 0:
                return -1
            elif sum_remaining == 0:
                return 0
            elif mem[sum_remaining]:
                return mem[sum_remaining]
            else:
                min_coins = amount + 1
                for coin in coins:
                    if sum_remaining - coin >= 0:
                        prev_coins = make_change(sum_remaining - coin, coins, mem)
                        curr_coins = 1 + prev_coins
                        if curr_coins > 0 and curr_coins < min_coins:
                            min_coins = curr_coins
                mem[sum_remaining] = min_coins
                return mem[sum_remaining]
        mem = [None] * (amount + 1)
        ans = make_change(amount, coins, mem)
        if ans == amount + 1:
            return -1
        else:
            return ans
