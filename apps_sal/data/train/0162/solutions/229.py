class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        L1=len(text1)
        L2=len(text2)
        A=[ [0]*(L2+1) for i in range(L1+1)]

        ##print(A)
        Max=0
        ##print(L1,L2)
        for i in range(L1,-1,-1):
                for j in range(L2,-1,-1):
                    if i<L1 and j<L2:
                        ##print(i,j)
                        if text1[i]==text2[j]:
                                A[i][j]= A[i+1][j+1]+1
                        else: A[i][j]=max(A[i][j+1],A[i+1][j])
                    if Max<A[i][j]: Max=A[i][j]


        ##print(A[2][3])
        return A[i][j]
    
        
        
        

