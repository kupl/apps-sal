class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        dp = [0] + [-target]*target
        for t in range(1, target+1):
            dp[t] = max([dp[t-i] for i in cost if i<=t]+[dp[t]]) + 1
        if dp[-1]<=0: return '0'
        res = ''
        for i in range(8, -1, -1):
            while target>=cost[i] and dp[target-cost[i]]==dp[target]-1:
                res += str(i+1)
                target -= cost[i]
        return res
