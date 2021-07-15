class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        
#         d = {}
#         for i in range(len(A)):
#             for j in range(i+1,len(A)):
#                 diff = A[j] - A[i]
                
#                 if (i,diff) in d:
#                     d[(j,diff)] = d[(i,diff)] + 1
                    
#                 else:
#                     d[(j,diff)] = 2
                    
#         print(d)
#         return max(d.values())
    
        n=len(A)
        dp={}
        for i in range(n):
            for j in range(i+1,n):
                dif = A[j]-A[i]
                if (i,dif) in dp :
                    dp[(j,dif)]=dp[(i,dif)]+1
                else:
                    dp[(j,dif)]=2
        return max(dp.values())
