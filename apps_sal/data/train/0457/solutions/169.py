class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        result = -1

        def helper(coins: List[int], pos: int, left: int, current: int):
            nonlocal result
            if left % coins[pos] == 0:
                if result == -1 or result > current + left // coins[pos]:
                    result = current + left // coins[pos]
                return

            if pos == len(coins) - 1:
                return

            for k in range(left // coins[pos], -1, -1):
                new_amount = left - coins[pos] * k
                new_count = current + k
                if result != -1 and result < new_count + (new_amount + coins[pos + 1] - 1) / coins[pos + 1]:
                    break
                helper(coins, pos + 1, left - coins[pos] * k, current + k)

        helper(coins, 0, amount, 0)
        return result
