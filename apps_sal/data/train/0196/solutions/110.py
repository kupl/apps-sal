class Solution:

    def maxSubarraySumCircular(self, A: List[int]) -> int:
        N = len(A)
        P = [0]
        for _ in range(2):
            for x in A:
                P.append(P[-1] + x)
        ans = A[0]
        deque = collections.deque([0])
        for j in range(1, len(P)):
            while deque[0] < j - N:
                deque.popleft()
            ans = max(ans, P[j] - P[deque[0]])
            while deque and P[j] <= P[deque[-1]]:
                deque.pop()
            deque.append(j)
        return ans
