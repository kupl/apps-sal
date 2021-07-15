class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        width = 0
        icandidate = [0]
        for i in range(len(A)):
            if A[i] < A[icandidate[-1]]:
                icandidate.append(i)
        for j in range(len(A) - 1, -1, -1):
            while icandidate and A[icandidate[-1]] <= A[j]:
                width = max(width, j - icandidate.pop())
        return width
