class Solution:
    def longestMountain(self, A: List[int]) -> int:
        res = up = down = 0
        for i in range(1, len(A)):
            if down and A[i - 1] < A[i] or A[i - 1] == A[i]:  # to check if we found down and the next is up
                up = down = 0  # reset for next down and make sure we are counting right up's
            up += A[i - 1] < A[i]
            down += A[i - 1] > A[i]
            if up and down:
                res = max(res, up + down + 1)
        return res
