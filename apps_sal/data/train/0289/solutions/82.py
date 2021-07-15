class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        
        sumL = sum(A[:L])
        sumM = sum(A[L:(L+M)])
        res = sumL + sumM
        for j in range(L+M, len(A)):
            sumM += A[j]-A[j-M]
            res = max(res, sumL+sumM)
        
        for i in range(L, len(A)):
            sumL += A[i]-A[i-L]
            if i-L+1 >= M:
                sumM = sum(A[:M])
                res = max(res, sumL+sumM)
                for j in range(M, i-L+1):
                    sumM += A[j]-A[j-M]
                    res = max(res, sumL+sumM)
            if i <= len(A)-M-1:
                sumM = sum(A[(i+1):(i+1+M)])
                for j in range(i+1+M, len(A)):
                    sumM += A[j]-A[j-M]
                    res = max(res, sumL+sumM)
        return res

