class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        memo = {}
        post_sum = [0] * (n + 1)
        for i in range(n)[::-1]:
            post_sum[i] = stoneValue[i] + post_sum[i + 1]
        
        def dfs(i):
            if i >= n:
                return 0
            
            if i in memo:
                return memo[i]
            
            res = float('-inf')
            cur = 0
            for j in range(i, min(i + 3, n)):
                cur += stoneValue[j]
                res = max(res, cur + post_sum[j + 1] - dfs(j + 1))
            
            memo[i] = res
            return res
        
        res = dfs(0)
        if res * 2 == post_sum[0]:
            return 'Tie'
        
        if res * 2 > post_sum[0]:
            return 'Alice'
        
        return 'Bob'

