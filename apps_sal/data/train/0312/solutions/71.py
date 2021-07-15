from collections import deque


class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        d = deque()
        n = len(A)
        res = n+1

        prefixArr = [0] * (n + 1)

        for i in range(n):
            prefixArr[i + 1] = A[i] + prefixArr[i]

        for end in range(n+1):
            while d and prefixArr[end] - prefixArr[d[0]] >= K:
                res = min(res, end - d.popleft())
            while d and prefixArr[d[-1]] >= prefixArr[end]:
                d.pop()
            d.append(end)

        return -1 if res == n+1 else res


