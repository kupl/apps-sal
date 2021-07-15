class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        ans = 0
        sub1 = 0
        for i in range(L-1):
            sub1 += A[i]
        for i in range(L-1, len(A)):
            sub1 += A[i]
            if i >= L+M-1:
                sub2 = 0
                for j in range(M-1):
                    sub2 += A[j]
                for j in range(M-1, i-L+1):
                    sub2 += A[j]
                    ans = max(ans, sub1+sub2)
                    sub2 -= A[j-M+1]
            
            if i <= len(A)-M-1:
                sub2 = 0
                for j in range(i+1, i+M):
                    sub2 += A[j]
                for j in range(i+M, len(A)):
                    sub2 += A[j]
                    ans = max(ans, sub1+sub2)
                    sub2 -= A[j-M+1]
            sub1 -= A[i-L+1]
        return ans
