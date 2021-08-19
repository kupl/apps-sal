class Solution:

    def dieSimulator(self, n: int, R: List[int]) -> int:
        (D, R, S, m) = ([[0] * 7 for _ in range(n)], [0] + R, set(range(1, 7)), 10 ** 9 + 7)

        def dfs(L, d):
            if L >= n:
                return 1 if L == n else 0
            c = 0
            if D[L][d]:
                return D[L][d]
            for i in S - {d}:
                for j in range(1, R[i] + 1):
                    c += dfs(L + j, i)
            D[L][d] = c
            return c
        return dfs(0, 0) % m
