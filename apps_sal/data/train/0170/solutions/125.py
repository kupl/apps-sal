class Solution:

    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        A = arr
        N = len(A)
        j = N - 1
        while j >= 1 and A[j - 1] <= A[j]:
            j -= 1
        res = j
        for i in range(N):
            if i >= j or (i > 0 and A[i] < A[i - 1]):
                break
            while j < N and A[i] > A[j]:
                j += 1
            res = min(res, j - i - 1)
        return res
