class Solution:
    def longestMountain(self, A: List[int]) -> int:
        res = up = down = 0
        for i in range(1, len(A)):
            if down and A[i - 1] < A[i] or A[i - 1] == A[i]:
                up = down = 0
            if A[i - 1] < A[i]:
                up += 1
            else:
                down += 1
            if up and down:
                res = max(res, up + down + 1)
        return res
