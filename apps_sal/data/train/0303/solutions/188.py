class Solution:

    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        memo = {}

        def dfs(i):
            if i >= n:
                return 0
            if i in memo:
                return memo[i]
            res = float('-inf')
            cur_max = float('-inf')
            for j in range(i, min(i + k, n)):
                cur_max = max(cur_max, arr[j])
                res = max(res, cur_max * (j - i + 1) + dfs(j + 1))
            memo[i] = res
            return res
        return dfs(0)
