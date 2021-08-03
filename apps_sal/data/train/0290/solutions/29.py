class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        dp = {}

        def dfs(i, j):
            if(i > j):
                return 0
            if((i, j) in dp):
                return dp[(i, j)]
            ans = float('inf')
            iscut = False
            for cut in cuts:
                if(i < cut and j > cut):
                    temp = dfs(i, cut) + dfs(cut, j)
                    ans = min(temp, ans)
                    iscut = True
            if(not iscut):
                dp[(i, j)] = 0
            else:
                dp[(i, j)] = ans + j - i
            return dp[(i, j)]
        return dfs(0, n)
