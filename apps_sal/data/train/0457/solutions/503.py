class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        seen = level = {0}
        coin_n = 0

        while level:
            if amount in level:
                return coin_n

            level = {val + coin for val in level for coin in coins if val + coin <= amount} - seen
            seen |= level

            coin_n += 1

        return -1
