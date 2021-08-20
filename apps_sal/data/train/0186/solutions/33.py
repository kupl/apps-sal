from functools import lru_cache


class Solution:

    def largestNumber(self, cost: List[int], target: int) -> str:
        ss = set()
        for (i, c) in enumerate(reversed(cost)):
            if c not in ss:
                ss.add(c)
            else:
                cost[~i] = float('inf')
        cost = list(((cost[i], str(i + 1)) for i in range(9) if cost[i] != float('inf')))
        dp = [[] for _ in range(target + 1)]
        for i in range(1, target + 1):
            for (c, d) in cost:
                if i - c == 0 or (i - c > 0 and len(dp[i - c])):
                    tmp = sorted(dp[i - c] + [d], reverse=1)
                    if len(dp[i - c]) + 1 > len(dp[i]):
                        dp[i] = tmp
                    elif len(dp[i - c]) + 1 == len(dp[i]):
                        if tmp > dp[i]:
                            dp[i] = tmp
        return ''.join(dp[-1]) if dp[-1] else '0'
