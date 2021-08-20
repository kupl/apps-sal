class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        coins = set(coins)
        d = {}
        if amount == 0:
            return 0

        def solve(amt):
            if amt in d:
                return d[amt]
            if amt <= 0:
                return -1
            if amt in coins:
                d[amt] = 1
                return d[amt]
            poss = []
            for c in coins:
                search = amt - c
                if search < 1:
                    continue
                val = solve(search)
                if val != -1:
                    poss.append(val)
            if len(poss) != 0:
                d[amt] = 1 + min(poss)
            else:
                d[amt] = -1
            return d[amt]
        return solve(amount)
