class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        dp = [[] for i in range(len(tree))]
        dp[-1] = [1, 1, [tree[-1]]]
        res = 1
        for i in reversed(list(range(len(tree)-1))):
            if tree[i] == tree[i+1]:
                dp[i] = [dp[i+1][0]+1, dp[i+1][1]+1, dp[i+1][2]]
            elif len(dp[i+1][2]) == 1:
                dp[i] = [dp[i+1][0]+1, 1, [tree[i], dp[i+1][2][0]]] 
            elif tree[i] in dp[i+1][2]:
                dp[i] = [dp[i+1][0]+1, 1, dp[i+1][2]]
            else:
                dp[i] = [1+dp[i+1][1], 1, [tree[i], tree[i+1]]]
            res = max(res, dp[i][0])
        return res

