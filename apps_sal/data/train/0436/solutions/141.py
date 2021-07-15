class Solution:
    def minDays(self, n: int) -> int:
        queue = [(n,0)]
        visited = set()
        while queue:
            remain, day = queue.pop(0)
            if remain == 0: return day
            if remain % 2 == 0 and remain//2 not in visited:
                queue.append((remain//2, day+1))
                visited.add(remain//2)
            if remain % 3 == 0 and remain//3 not in visited:
                queue.append((remain//3, day+1))
                visited.add(remain//3)
            if remain-1 not in visited:
                queue.append((remain - 1, day+1))
            
            
        # dp = {}
        # dp[0] = 0
        # dp[1] = 1
        # for i in range(2, n+1):
        #     if i % 2 == 0 and i % 3 == 0:
        #         dp[i] = min(dp[i//2], dp[i//3], dp[i-1]) + 1
        #     elif i % 2 == 0:
        #         dp[i] = min(dp[i//2], dp[i-1]) + 1
        #     elif i % 3 == 0:
        #         dp[i] = min(dp[i//3], dp[i-1]) + 1
        #     else:
        #         dp[i] = dp[i-1] + 1
        # return dp[n]

