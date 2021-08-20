class Solution:

    def minCost(self, s: str, cost: List[int]) -> int:

        def num(s):
            return ord(s) - ord('a')
        dp = [0, 0]
        n = len(s)
        C = 1
        for i in range(1, n):
            if s[i] == s[i - 1]:
                if C == 1:
                    max_c = max(cost[i - 1], cost[i])
                    sum_c = dp[-1] + cost[i - 1] + cost[i]
                else:
                    max_c = max(max_c, cost[i])
                    sum_c += cost[i]
                c = sum_c - max_c
                C += 1
                dp.append(c)
            else:
                C = 1
                dp.append(dp[-1])
        return dp[-1]
