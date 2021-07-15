class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dic={}
        for i in range(len(A)):
            for j in range(i+1,len(A)):
                dic[(j,A[j]-A[i])]=dic.get((i,A[j]-A[i]),1)+1
        return max(dic.values())
