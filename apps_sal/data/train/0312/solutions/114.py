from collections import deque


class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:

        n = len(A)
        B = [0 for _ in range(n + 1)]
        for i in range(n):
            B[i + 1] = A[i] + B[i]

        res = n + 1
        d = deque()
        for j in range(n + 1):
            while d and B[j] - B[d[0]] >= K:
                res = min(res, j - d[0])
                d.popleft()
            while d and B[d[-1]] > B[j]:
                d.pop()
            d.append(j)

        return res if res <= n else -1
