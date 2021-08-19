from bisect import bisect_left
from itertools import accumulate


class Solution:

    def shortestSubarray(self, A: List[int], K: int) -> int:
        MAX_L = 10 ** 9
        res = Solver(A, K, MAX_L).solve(0, len(A) - 1)
        return res if res < MAX_L else -1


class Solver:

    def __init__(self, A, K, MAX_L):
        self.A = A
        self.K = K
        self.MAX_L = MAX_L

    def solve(self, i, j):
        if i == j:
            return 1 if self.A[i] >= self.K else self.MAX_L
        if sum((abs(self.A[v]) for v in range(i, j + 1))) < self.K:
            return self.MAX_L
        m = (i + j) // 2
        return min([self.solve(i, m), self.solve(m + 1, j), self.solve_pivot(i, j, m)])

    def bin_search(self, arr, v):
        if arr[-1][0] < v:
            return self.MAX_L
        i = bisect_left(arr, (v, 0))
        return arr[i][1]

    def solve_pivot(self, i, j, m):
        left = self.min_arr(m, i - 1, -1)
        right = self.min_arr(m + 1, j + 1, 1)
        ans = self.MAX_L
        for (l_v, l_cnt) in left:
            r_cnt = self.bin_search(right, self.K - l_v)
            ans = min(ans, l_cnt + r_cnt)
        return ans

    def min_arr(self, start, stop, step):
        res = []
        acc = 0
        for i in range(start, stop, step):
            acc += self.A[i]
            if not res or acc > res[-1][0]:
                res.append((acc, abs(start - i) + 1))
        return res
