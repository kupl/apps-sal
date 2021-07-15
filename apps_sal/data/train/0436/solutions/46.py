class Solution:
    # @lru_cache()
    # ^
    # what's this?
    def minDays(self, n: int) -> int:
        # # Method 1: DP -> TLE
        self.m = 10000
        self.dp = [0, 1] + [float('inf')] * (self.m-1)
        for i in range(2,self.m+1):
            v = []
            v.append(self.dp[i-1])
            if i % 2 == 0:
                v.append(self.dp[i//2])
            if i % 3 == 0:
                v.append(self.dp[i//3])
            self.dp[i] = min(v) + 1
        # return dp[-1]
        
        # # Method 3: Gready -> Dijkstra?
        def dfs(n):
            # print(n)
            if n <= self.m:
                return self.dp[n]
            else:
                return 1 + min(n%2 + dfs(n//2), n%3 + dfs(n//3))
        return dfs(n)
        
        # # Method 2: DP -> TLE
        # dp = [0, 1] + [float('inf')] * (n-1)
        # for i in range(1, n+1):
        #     if i+1 <= n:
        #         dp[i+1] = min(dp[i+1], dp[i] + 1)
        #     if i*2 <= n:
        #         dp[i*2] = min(dp[i*2], dp[i] + 1)
        #     if i*3 <= n:
        #         dp[i*3] = min(dp[i*3], dp[i] + 1)
        # return dp[-1]
        
        # # Method 4: DFS
        # # DFS
        # def dfs(n):
        #     if n == 1:
        #         return 1
        #     else:
        #         print(n)
        #         if n % 3 == 0:
        #             print(\"case 3\")
        #             v3 = dfs(n//3) + 1
        #             self.ans.append(v3)
        #         if n % 2 == 0:
        #             print('case 2')
        #             v2 = dfs(n//2) + 1
        #             self.ans.append(v2)
        #         if n - 1 > 1:
        #             print('case 1')
        #             v1 = dfs(n-1) + 1
        #             self.ans.append(v1)
        # dfs(n)
        # return min(self.ans)

