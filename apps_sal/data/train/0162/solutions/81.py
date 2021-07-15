class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        mem = {}
        def dfs(l, r):
            if((l, r) in mem):
                return mem[(l, r)]
            if(l == len(text1) or r == len(text2)):
                return 0
            ans = 0
            if(text1[l] == text2[r]):
                ans = 1+dfs(l+1, r+1)
            else:
                ans = max(dfs(l+1, r), dfs(l, r+1))
            mem[(l, r)] = ans
            return ans
        return dfs(0, 0)
