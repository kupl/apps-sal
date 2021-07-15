class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        return self.helper(0,0,text1,text2,memo)
        
    def helper(self,index_1,index_2,text1,text2,memo):
        if (index_1 == len(text1) or index_2 == len(text2)):
            return 0
        elif (index_1,index_2) in memo:
            return memo[(index_1,index_2)]
        else:
            if (text1[index_1] == text2[index_2]):
                ans = 1 + self.helper(index_1 + 1,index_2 + 1,text1,text2,memo)
            else:
                ans = max(self.helper(index_1 + 1,index_2,text1,text2,memo),
                          self.helper(index_1,index_2 + 1,text1,text2,memo))
            memo[(index_1,index_2)] = ans
            return ans

