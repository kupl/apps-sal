class Solution:
    def findLengthOfShortestSubarray(self, A):

        N = len(A)
        j = N - 1
        while j and A[j - 1] <= A[j]:
            j -= 1

        ans = j
        for i in range(j):
            if i and A[i - 1] > A[i]:
                break
            while j < N and A[i] > A[j]:
                j += 1
            ans = min(ans, j - i - 1)

        return ans
