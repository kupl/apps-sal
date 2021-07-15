class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1, l2 = len(text1), len(text2)
        if l1 == 0 or l2 == 0:
            return 0
        dp = [0 for _ in range(l1+1)]
        for i in range(l2):
            temp = [n for n in dp]
            curMax = 0
            for j in range(1, l1+1):
                if temp[j-1] > curMax:
                    curMax = temp[j-1]
                if text2[i] == text1[j-1]:
                    dp[j] = curMax + 1
            
        return max(dp)
        

