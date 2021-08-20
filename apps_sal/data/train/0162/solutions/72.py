class Solution:

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = [[-1] * (len(text2) + 1) for _ in range(len(text1) + 1)]

        def dfs(t1, t2):
            (n1, n2) = (len(t1), len(t2))
            if memo[n1][n2] != -1:
                return memo[n1][n2]
            if n1 == 0 or n2 == 0:
                return 0
            if t1[-1] == t2[-1]:
                res = dfs(t1[:-1], t2[:-1]) + 1
            else:
                res = max(dfs(t1[:-1], t2), dfs(t1, t2[:-1]))
            memo[n1][n2] = res
            return res
        dfs(text1, text2)
        return memo[-1][-1]
