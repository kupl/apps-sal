class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        N = len(A)

        # Compute P[j] = sum(B[:j]) for the fixed array B = A+A
        P = [0]
        for _ in range(2):
            for x in A:
                P.append(P[-1] + x)

        # Want largest P[j] - P[i] with 1 <= j-i <= N
        # For each j, want smallest P[i] with i >= j-N
        ans = A[0]
        deque = collections.deque([0]) # i's, increasing by P[i]
        for j in range(1, len(P)):
            # If the smallest i is too small, remove it.
            while deque[0] < j-N:
                deque.popleft()

            # The optimal i is deque[0], for cand. answer P[j] - P[i].
            ans = max(ans, P[j] - P[deque[0]])

            # Remove any i1's with P[i2] <= P[i1].
            while deque and P[j] <= P[deque[-1]]:
                deque.pop()

            deque.append(j)

        return ans

