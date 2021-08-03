from collections import deque


class Solution:
    def constrainedSubsetSum(self, A: List[int], k: int) -> int:
        d = deque()
        for i in range(len(A)):
            A[i] += d[0] if d else 0
            while d and d[-1] < A[i]:
                d.pop()
            if A[i] > 0:
                d.append(A[i])
            if i >= k and d and d[0] == A[i - k]:
                d.popleft()
        return max(A)
