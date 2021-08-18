

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        level = seen = {0}
        number = 0
        while level:
            if amount in seen:
                return number
            level = {pre_amount + coin for pre_amount in level for coin in coins if pre_amount + coin <= amount}
            seen.update(level)
            number += 1
        return -1
