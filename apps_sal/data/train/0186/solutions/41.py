class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        t = target
        dp = [ ['0'] for _ in range(t + 1)] 
        dp[0] = ['']
        for i in range(1, t + 1):
            for j in range(9):
                l1 = len(dp[i]) 
                l1 = 0 if dp[i] == ['0'] else l1
                l2 = len(dp[i - cost[j]]) + 1 if i>=cost[j] else 0
                c = dp[i - cost[j]] if i>=cost[j] else ['0']
                # print(l1,l2)
                if l1 <= l2:
                    dp[i] = c + [str(j + 1)] if c != ['0'] else ['0']
                # if i == t:
                #     print(dp[i], c, l1, l2)
               
            # print(dp[0:][j])
        # print(dp)
        ans = ''.join(sorted(dp[t])[::-1])
        return ans
