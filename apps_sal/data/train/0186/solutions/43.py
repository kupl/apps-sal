class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        d = {i: -1 for i in cost}
        for i in range(1, len(cost) + 1):
            d[cost[i - 1]] = max(d[cost[i - 1]], i)
        dp = ['-1'] * (target + 1)
        cost = list(set(cost))
        cost.sort()
        for i in d:
            try:
                dp[i] = str(d[i])
            except:
                pass
        for i in range(1, target + 1):
            for j in cost:
                if i - j > 0:
                    if dp[i - j] != '-1':
                        dp[i] = str(max(int(dp[i - j] + str(d[j])), int(dp[i])))
                    else:
                        try:
                            dp[i] = str(max(int(dp[i]), d[i]))
                        except:
                            pass
                else:
                    break
        if dp[target] == '-1':
            return '0'
        return dp[target]
