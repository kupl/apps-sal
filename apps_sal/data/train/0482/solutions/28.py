class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        
        # use dynamic programming 
        # dp[i][j] denotes the cost of constructing a tree from arr[i:j + 1]
        n = len(arr)
        dp = [ [0 for _ in range(n)] for _ in range(n)]
        
        # the cost of constructing a tree from one value is always 0 
        for i in range(n):
            dp[i][i] = 0 
        for i in range(n - 1):
            dp[i][i + 1] = arr[i] * arr[i + 1]
        
        # now work iteratively for subarraies of length: 2, 3, ..., n - 1
        for l in range(2, n + 1):
            # (i, j) is the boundary
            for i in range(n - l):
                j = i + l
                # split the (i, j) array into (i, k) and (k, j) subarraies
                dp[i][j] = float('inf')
                for k in range(i + 1, j + 1):
                    q = dp[i][k - 1] + dp[k][j] + max(arr[i:k]) * max(arr[k: j + 1])
                    if q < dp[i][j]:
                        dp[i][j] = q
                
        return dp[0][-1]
                    
        

