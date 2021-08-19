class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:

        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 0

        @lru_cache(maxsize=None)
        def dp(n):

            if n == 0:
                return (0, 0)

            last = dp(n - 1)  # (val, lastword_index)
            ans = 0
            lastans = last[0]
            last_index = last[1]

            next_index = 0

            if s[last_index] == s[n]:
                if cost[last_index] <= cost[n]:
                    ans = lastans + cost[last_index]
                    next_index = n
                    #print(n, last_index, ans)
                else:
                    ans = lastans + cost[n]
                    next_index = last_index
                    #print(n, n, ans)
            else:
                ans = lastans
                next_index = n

            return (ans, next_index)

        return dp(len(s) - 1)[0]
