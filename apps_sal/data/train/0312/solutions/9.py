from collections import deque


class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        if not A:
            return -1

        sum_A = [0]
        for a in A:
            sum_A.append(a + sum_A[-1])

        d = deque()
        res = len(A) + 1
        for i in range(len(sum_A)):
            while d and sum_A[i] <= sum_A[d[-1]]:
                d.pop()

            while d and sum_A[i] - sum_A[d[0]] >= K:
                res = min(res, i - d.popleft())

            d.append(i)

        return res if res != len(A) + 1 else -1
