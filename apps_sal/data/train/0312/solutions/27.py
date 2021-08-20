from collections import deque


class Solution:

    def shortestSubarray(self, A: List[int], K: int) -> int:
        d = deque([(0, 0)])
        curr = 0
        n = len(A)
        res = n + 1
        for r in range(n):
            curr += A[r]
            while d and curr - d[0][1] >= K:
                res = min(res, r - d.popleft()[0] + 1)
            while d and curr <= d[-1][1]:
                d.pop()
            d.append((r + 1, curr))
        return res if res != n + 1 else -1
