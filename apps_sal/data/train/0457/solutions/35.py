class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        visited = set([amount])
        candidates = [amount]
        res = 0
        while candidates:
            res += 1
            next_candidates = []
            for candidate in candidates:
                for coin in coins:
                    if candidate - coin == 0:
                        return res
                    elif candidate - coin > 0 and candidate - coin not in visited:
                        next_candidates.append(candidate - coin)
                        visited.add(candidate - coin)
            candidates = next_candidates
        return -1
