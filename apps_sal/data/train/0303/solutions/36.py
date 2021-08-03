class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        def dfs(i, j, max_num=0):
            if i == -1:
                return max_num * j

            if opt[i][j] == -1:
                a, b = 0, 0
                if j < K:
                    a = dfs(i - 1, j + 1, max(max_num, A[i]))
                b = j * max_num + dfs(i - 1, 1, A[i])
                opt[i][j] = max(a, b)
            return opt[i][j]

        n = len(A)
        opt = [[-1] * (K + 1) for _ in range(n)]
        return dfs(n - 1, 0)
