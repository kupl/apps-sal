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
                

