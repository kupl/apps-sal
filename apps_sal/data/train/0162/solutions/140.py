class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #hashh={}
        def helper(text1,text2,i,j,hashh):
            if i>=len(text1) or j>=len(text2):
                return 0
            leftElement=text1[i]
            rightElement=text2[j]
            if (i,j) in hashh:
                return hashh[(i,j)]
            if text1[i]==text2[j]:
                hashh[(i,j)]=1+helper(text1,text2,i+1,j+1,hashh)
            else:
                temp1=helper(text1,text2,i+1,j,hashh)
                temp2=helper(text1,text2,i,j+1,hashh)
                hashh[(i,j)]=max(temp1,temp2)
            return hashh[(i,j)]
        return helper(text1,text2,0,0,{})
