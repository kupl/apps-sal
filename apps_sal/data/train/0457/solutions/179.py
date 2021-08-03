class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def _fewest(cs, amt):
            nonlocal memo
            if amt not in memo:
                if amt < 0:
                    memo[amt] = -1
                elif amt == 0:
                    memo[amt] = 0
                else:
                    fewest = -1
                    for c in cs:
                        f = _fewest(cs, amt - c)
                        if f != -1 and (fewest == -1 or f + 1 < fewest):
                            fewest = f + 1
                    memo[amt] = fewest
            return memo[amt]

        return _fewest(coins, amount)
