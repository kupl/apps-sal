class Solution:

    def longestMountain(self, A: List[int]) -> int:
        if len(A) < 3:
            return 0
        (up, down, Max) = ([1] * len(A), [1] * len(A), 0)
        for i in range(1, len(A)):
            if A[i] > A[i - 1]:
                up[i] = up[i - 1] + 1
        for i in range(len(A) - 2, -1, -1):
            if A[i] > A[i + 1]:
                down[i] = down[i + 1] + 1
        for i in range(1, len(A) - 1):
            if A[i - 1] < A[i] > A[i + 1]:
                Max = max(Max, up[i] + down[i] - 1)
        return Max
