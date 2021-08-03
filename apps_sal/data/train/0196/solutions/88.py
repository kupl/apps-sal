class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        n = len(A)

        ans = -float('inf')
        currmax = -float('inf')
        for i in range(n):
            currmax = max(currmax + A[i], A[i])
            ans = max(ans, currmax)

        right_sums = [0] * n
        right_sums[-1] = A[-1]
        for i in range(1, n):
            right_sums[n - 1 - i] = right_sums[n - i] + A[n - i - 1]

        maxright = [0] * n
        maxright[-1] = right_sums[-1]
        for i in range(1, n):
            maxright[n - i - 1] = max(maxright[n - i], right_sums[n - i - 1])

        lefts = 0
        for i in range(n - 2):
            lefts += A[i]
            ans = max(ans, lefts + maxright[i + 2])

        return ans
