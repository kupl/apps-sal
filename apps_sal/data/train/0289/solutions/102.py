class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        cur_max_l = max_l = sum(A[:L])
        ans = max_l + sum(A[L:L+M])
        
        for i in range(L, len(A) - M):
            cur_max_l = cur_max_l + A[i] - A[i-L]
            max_l = max(max_l, cur_max_l)
            
            ans = max(ans, max_l + sum(A[i+1:i+1+M]))
        
        cur_max_m = max_m = sum(A[:M])
        ans = max(ans, max_m + sum(A[M:L+M]))
        
        for i in range(M, len(A) - L):
            cur_max_m = cur_max_m + A[i] - A[i-M]
            max_m = max(max_m, cur_max_m)
            
            ans = max(ans, max_m + sum(A[i+1:i+1+L]))
        
        return ans
