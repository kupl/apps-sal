class Solution(object):
    def maxTurbulenceSize(self, A):
        # rule out all same element
        if A.count(A[0]) == len(A):
            return 1
        if len(A) < 2:
            return len(A)

        # sliding window
        start = 0
        end = 0
        max_res = 0

        while end < len(A) - 1:
            # check alternate sign
            if (A[end - 1] - A[end]) * (A[end] - A[end + 1]) < 0:
                end += 1
            # update the max and sliding window to start = end, end = start + 1
            else:
                max_res = max(max_res, end - start + 1)
                start = end
                end = start + 1
        # since we are breaking the check on end - 1, we need to check the last length
        return max(max_res, end - start + 1)
