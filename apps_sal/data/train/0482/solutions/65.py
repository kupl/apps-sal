class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        table = {}
        def dp(i, j):
            if j == i:
                return 0
            if j == i+1:
                return arr[i] * arr[j]
            if (i, j) in table:
                return table[(i, j)]
            res = float('inf')
            for k in range(i, j):
                res = min(res, dp(i, k) + dp(k+1, j) + max(arr[i:k+1]) * max(arr[k+1:j+1]))
            table[(i, j)] = res
            return res
        return dp(0, len(arr)-1)
