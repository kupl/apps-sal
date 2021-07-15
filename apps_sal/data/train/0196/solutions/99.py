class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        pre = 0
        rtn = float('-inf')
        if max(A) <= 0:
            return max(A)
        
        for i in range(len(A)):
            pre += A[i]
            if pre <= 0:
                pre = 0
            else:
                rtn = max(rtn, pre)
        left_sum = [0]*(len(A)+1)
        left = 0
        for i in range(len(A)):
            left += A[i]
            left_sum[i+1] = max(left, left_sum[i])
        right = 0
        for j in reversed(range(len(A))):
            right += A[j]
            rtn = max(rtn, right+left_sum[j])
        return rtn
