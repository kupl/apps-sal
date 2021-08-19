class Solution:

    def maxSubarraySumCircular(self, A: List[int]) -> int:
        N = len(A)
        ans = float('-inf')
        cur = 0
        for x in A:
            cur = x + max(cur, 0)
            ans = max(ans, cur)
        rightsums = [None] * N
        rightsums[-1] = A[-1]
        for i in range(N - 2, -1, -1):
            rightsums[i] = rightsums[i + 1] + A[i]
        maxright = [None] * N
        maxright[-1] = rightsums[-1]
        for i in range(N - 2, -1, -1):
            maxright[i] = max(maxright[i + 1], rightsums[i])
        leftsum = 0
        for i in range(N - 2):
            leftsum += A[i]
            ans = max(ans, leftsum + maxright[i + 2])
        return ans
