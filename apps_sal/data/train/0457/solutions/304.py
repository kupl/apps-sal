class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def backtrack(memo, curr=amount):
            if curr == 0:
                return 0
            if memo.get(curr):
                return memo[curr]
            minimum = math.inf
            for coin in coins:
                if curr - coin < 0:
                    continue
                res = backtrack(memo, curr - coin)
                minimum = min(res, minimum)
            minimum = minimum if minimum == math.inf else minimum + 1
            memo[curr] = minimum
            return minimum
        ans = backtrack(memo)
        if ans == math.inf:
            return -1
        return ans
