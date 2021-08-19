from collections import deque


class Solution:
    def constrainedSubsetSum(self, A: List[int], k: int) -> int:
        Q = deque([(0, A[0])])  # decreasing
        running_max = A[0]
        for i in range(1, len(A)):
            if Q[0][0] < i - k:
                Q.popleft()
            maxsum_of_subseq_ends_at_i = A[i] + max(Q[0][1], 0)
            running_max = max(maxsum_of_subseq_ends_at_i, running_max)
            while Q and Q[-1][1] <= maxsum_of_subseq_ends_at_i:
                Q.pop()
            Q.append((i, maxsum_of_subseq_ends_at_i))

        return running_max
