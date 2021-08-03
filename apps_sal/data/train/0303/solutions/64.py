class Solution:
    def maxSumAfterPartitioning(self, A: List[int], k: int) -> int:
        def dfs(i, j, max_num=0):
            if i == -1:
                return max_num * j

            if (i, j, max_num) not in opt:
                ans = 0
                if j < k:
                    ans = max(ans, dfs(i - 1, j + 1, max(max_num, A[i])))
                ans = max(ans, j * max_num + dfs(i - 1, 1, A[i]))
                opt[(i, j, max_num)] = ans
            return opt[(i, j, max_num)]

        n = len(A)
        opt = dict()
        return dfs(n - 1, 0)
