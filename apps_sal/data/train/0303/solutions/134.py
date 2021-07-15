class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        memo = {}

        l_arr = len(arr)

        for chain_len in range(0, k, 1):
            for i in range(0, l_arr - chain_len, 1):
                memo[(i, i + chain_len)] = max(arr[i : i + chain_len + 1]) * (chain_len + 1)
        res_memo = {}    

        def dfs(idx):
            if idx == l_arr:
                return 0

            if idx in res_memo:
                return res_memo[idx]

            res_memo[idx] = max( memo[(idx, idx + j)] + dfs(idx + j + 1) for j in range(k) if idx + j < l_arr )
            return res_memo[idx]

        return dfs(0)
