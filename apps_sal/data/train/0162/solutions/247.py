class Solution:

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # recurrsion => lead to time exceeded
        # if not text1 or not text2:
        #     return 0
        # if text1[-1]==text2[-1]:
        #     return 1+self.longestCommonSubsequence(text1[0:-1],text2[0:-1])
        # elif text1[-1] != text2[-1]:
        #     t1 = self.longestCommonSubsequence(text1,text2[0:-1])
        #     t2 = self.longestCommonSubsequence(text1[0:-1],text2)
        #     return max(t1,t2)
        # memorized method
        #         n = len(text1)
        #         m = len(text2)
        #         arr = [[0] * (m+1) for _ in range(n+1)]
        #         return self.LCS(text1,text2,n,m,arr)

        #     def LCS(self,text1,text2,n,m,arr):
        #         if arr[n][m]:
        #             return arr[n][m]
        #         if n==0 or m==0:
        #             res = 0
        #         elif text1[n-1]==text2[m-1]:
        #             res = 1+self.LCS(text1,text2,n-1,m-1,arr)
        #         else:
        #             t1 = self.LCS(text1,text2,n,m-1,arr)
        #             t2 = self.LCS(text1,text2,n-1,m,arr)
        #             res = max(t1,t2)
        #         arr[n][m] = res
        #         return res
        # bottom-up method
        n, m = len(text1), len(text2)
        arr = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            for j in range(m + 1):
                if i == 0 or j == 0:
                    arr[i][j] = 0
                elif text1[i - 1] == text2[j - 1]:
                    arr[i][j] = 1 + arr[i - 1][j - 1]
                else:
                    arr[i][j] = max(arr[i - 1][j], arr[i][j - 1])
        return arr[-1][-1]  # arr[-1][-1]
