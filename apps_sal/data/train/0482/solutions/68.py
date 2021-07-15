class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        n = len(arr)
        self.memo = {}
        def dp(i, j):
            if i >= j:
                return 0
            if (i,j) not in self.memo:
                res = float('inf')
                for k in range(i, j):
                    res = min(res, dp(i, k) + dp(k+1, j) + max(arr[i:k+1]) * max(arr[k+1:j+1]))
                self.memo[(i,j)] = res
            return self.memo[(i,j)]
        return dp(0, n-1)
