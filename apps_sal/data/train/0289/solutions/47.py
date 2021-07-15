from functools import reduce
class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        
        def leftRight(lst, l, m):
            presum = reduce(lambda cum, cur: cum + [cur + cum[-1]], lst, [0])
            res = float('-inf')
            curL = presum[l]
            mxL = float('-inf')
            
            for i in range(l+m-1, len(lst)):
                if i > l + m - 1:
                    curL = curL - lst[i - (l+m)] + lst[i-m]
                    
                mxL = max(mxL, curL)
                res = max(res, mxL + presum[i+1] - presum[i-m+1])
            
            return res
        
        return max(leftRight(A, L, M), leftRight(A[::-1], L, M))

    # better: fix the middle part, keep track of the max of the left and right part of the middle part.

    # def maxSumTwoNoOverlap(self, A, L, M):
    #     for i in xrange(1, len(A)):
    #         A[i] += A[i - 1]
    #     res, Lmax, Mmax = A[L + M - 1], A[L - 1], A[M - 1]
    #     for i in xrange(L + M, len(A)):
    #         Lmax = max(Lmax, A[i - M] - A[i - L - M])
    #         Mmax = max(Mmax, A[i - L] - A[i - L - M])
    #         res = max(res, Lmax + A[i] - A[i - M], Mmax + A[i] - A[i - L])
    #     return res
                

