class Solution:

    def maxSubarraySumCircular(self, A: List[int]) -> int:
        n = len(A)
        ans = cur = float('-inf')
        for x in A:
            cur = x + max(cur, 0)
            ans = max(ans, cur)
        rightsums = [0] * n
        rightsums[-1] = A[-1]
        for i in range(n - 2, -1, -1):
            rightsums[i] = rightsums[i + 1] + A[i]
        maxright = [0] * n
        maxright[-1] = rightsums[-1]
        for i in range(n - 2, -1, -1):
            maxright[i] = max(maxright[i + 1], rightsums[i])
        leftsum = 0
        for i in range(n - 2):
            leftsum += A[i]
            ans = max(ans, leftsum + maxright[i + 2])
        return ans
