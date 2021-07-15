class Solution:
    def minDays(self, n: int) -> int:
        import math
        ans = {}

        def dfs(n, k):
            if n in ans.keys():
                return ans[n]
            if n == 1:
                return 1
            if k > 2 * math.log(n)//math.log(2) + 100:
                return 1e10
            if n == 0:
                return 0
            
            if n % 3 == 0:
                op3 = dfs(n//3, k+1) + 1
            else:
                op3 = 1e10

            if n % 2 == 0:
                op2 = dfs(n//2, k+1) + 1
            else:
                op2 = 1e10
        
            op1 = dfs(n-1, k+1)+1
            
            ans[n] = min(op1, min(op2, op3))
            
            return ans[n]
        
        return dfs(n, 0)
