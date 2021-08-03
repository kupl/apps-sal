class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        N = len(A)

        # Compute P[j] = sum(B[:j]) for the fixed array B = A+A
        P = [0]
        for _ in range(2):
            for x in A:
                P.append(P[-1] + x)

        ans = A[0]
        deque = collections.deque([0])
        for j in range(1, len(P)):
            if deque[0] < j - N:
                deque.popleft()

            # The optimal i is deque[0], for cand. answer P[j] - P[i].
            ans = max(ans, P[j] - P[deque[0]])

            # Remove any i1's with P[i2] <= P[i1].
            while deque and P[j] <= P[deque[-1]]:
                deque.pop()

            deque.append(j)

        return ans
