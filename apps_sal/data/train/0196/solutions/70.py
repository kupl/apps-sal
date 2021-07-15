class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        sums = sum(A)
        min_res = min_s = sys.maxsize
        max_res = max_s = -sys.maxsize
        n = len(A)
        for i in range(n):
            min_s = min(A[i], min_s + A[i])
            max_s = max(A[i], max_s + A[i])
            min_res = min(min_res, min_s)
            max_res = max(max_res, max_s)
        if min_res == sums:
            min_res = min(A)
        else:
            min_res = sums - min_res
        return max(min_res, max_res)
