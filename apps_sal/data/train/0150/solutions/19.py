class Solution:
    def partitionDisjoint(self, A: List[int]) -> int:
        maxval = A[0]
        v = A[0]
        disjoint = 0
        for i in range(len(A)):
            maxval = max(maxval,A[i])
            if A[i]<v:
                disjoint = i
                v = maxval
                
        return disjoint+1
                
        

