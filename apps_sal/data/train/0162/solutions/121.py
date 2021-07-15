class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def helper(i,j, dc):
            if i<0 or j<0:
                return 0
            if (i,j) in dc:
                return dc[(i,j)]
            
            if text1[i] == text2[j]:
                dc[(i,j)] = helper(i-1,j-1,dc) + 1
                return dc[(i,j)]
            else:
                dc[(i,j)] = max(helper(i-1,j,dc),
                                helper(i,j-1,dc))
                return dc[(i,j)]
        return helper(len(text1)-1,len(text2)-1,{})
            

