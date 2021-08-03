class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        round = 0
        d = set([0])
        while d or round == 0:
            round += 1
            d = set([coin + s for coin in coins for s in d if coin + s <= amount and coin + s not in d])
            if amount in d:
                return round
        return -1
