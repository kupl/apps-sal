class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        maxi = 0
        n = len(A)
        for i in range(1,n):
            A[i] += A[i-1]
        for i in range(n-L+1):
            for j in range(n-M+1):
                if (i>=j and i-j < M) or (i < j and j-i < L):
                    continue
                else:
                    istart = A[i-1] if i>0 else 0
                    jstart = A[j-1] if j>0 else 0
                    temp = A[i+L-1] - istart + A[j+M-1] - jstart
                    maxi = max(maxi,temp)
        return maxi
            

