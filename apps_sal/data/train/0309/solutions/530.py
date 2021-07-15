class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        
        if len(A)==0:
            return 0
        
        maxx=1
        arSubCounts = dict()
        
        for i in range(len(A)):
            for j in range(i+1,len(A)):
                diff = A[j]-A[i]
                arSubCounts[(j,diff)]=max(arSubCounts.get((j,diff),1),arSubCounts.get((i,diff),1)+1)
                maxx = max(arSubCounts[(j,diff)],maxx)
                
        return maxx

