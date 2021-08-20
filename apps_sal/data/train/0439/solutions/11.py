class Solution(object):

    def maxTurbulenceSize(self, A):
        if A.count(A[0]) == len(A):
            return 1
        if len(A) < 2:
            return len(A)
        start = 0
        end = 0
        max_res = 0
        while end < len(A) - 1:
            if (A[end - 1] - A[end]) * (A[end] - A[end + 1]) < 0:
                end += 1
            else:
                max_res = max(max_res, end - start + 1)
                start = end
                end = start + 1
        return max(max_res, end - start + 1)
