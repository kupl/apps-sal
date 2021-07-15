class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        sm = sum(A)
        mx = mn = cur_mx = cur_mn = A[0]
        for i in range(1, len(A)):
            cur_mn = min(cur_mn + A[i], A[i])
            mn = min(mn, cur_mn)
            cur_mx = max(cur_mx + A[i], A[i])
            mx = max(mx, cur_mx)
        return max(mx, (mn if mn==sm else (sm - mn)))
