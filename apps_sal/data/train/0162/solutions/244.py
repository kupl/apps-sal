class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        s1=text1
        s2=text2
        if len(s1)==0 or len(s2)==0:
            return 0
        rows=len(s1)+1
        cols=len(s2)+1
        arr=[[0 for i in range(cols)] for j in range(rows)]
        for i in range(len(s1)):
            for j in range(len(s2)):
                if s1[i]==s2[j]:
                    arr[i+1][j+1]=arr[i][j]+1
                if s1[i]!=s2[j]:
                    arr[i+1][j+1]=max(arr[i][j+1],arr[i+1][j])
        return(arr[-1][-1])

