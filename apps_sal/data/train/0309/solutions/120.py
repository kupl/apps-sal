class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        diffdict = {}
        max = 0
        
        for i in range(len(A)):
            
            for j in range(i):
                
                diff = A[i]-A[j]
                if diff not in diffdict:
                    diffdict[diff] = {i: 2}
                else:
                    if j in diffdict[diff]: 
                        diffdict[diff][i] = diffdict[diff][j] + 1
                    else:
                        diffdict[diff][i] = 2
                if diffdict[diff][i] > max:
                        max = diffdict[diff][i]
                    
        return  max
        

