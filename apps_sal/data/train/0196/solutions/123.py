class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        N = len(A)
        P = []
        P.append(0)
        for _ in range(2):
            for x in A:
                P.append(P[-1] + x)

        ans = A[0]
        queue = []
        queue.append(0)

        for j in range(1, len(P)):
            if queue[0] < j - N:
                queue.pop(0)
            ans = max(ans, P[j] - P[queue[0]])

            while queue and P[j] <= P[queue[-1]]:
                queue.pop()
            queue.append(j)

        return ans
