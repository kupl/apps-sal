class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @lru_cache(None)
        def lcs(s1,n,i,s2,m,j):
            if i>=n or j>=m:
                return 0
            if s1[i]==s2[j]:
                return 1 + lcs(s1,n,i+1,s2,m,j+1)
            return max(lcs(s1,n,i+1,s2,m,j),lcs(s1,n,i,s2,m,j+1))
        return lcs(text1,len(text1),0,text2,len(text2),0)

