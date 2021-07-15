class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        S=0
        negs=[]
        posmin=100
        negmax=-100
        for i in range(len(A)):
            S+=A[i]
            if A[i]<0:
                negs.append(A[i])
                negmax=max(negmax,A[i])
            else:
                posmin=min(posmin,A[i])
        if K is 0:
            return(S)
        negs.sort()
        if K <= len(negs):
            return(S-2*sum(negs[:K]))
        elif (K - len(negs))%2 is 0:
            return(S-2*sum(negs[:K]))
        elif posmin<-negmax:
            return(S-2*sum(negs[:K])-2*posmin)
        else:
            return(S-2*sum(negs[:K])+2*negmax)
