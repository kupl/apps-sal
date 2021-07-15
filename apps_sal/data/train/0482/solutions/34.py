class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        # solve(0, n) = min_i(max(a[:i])*max(a[i:])+solve(0, i) + solve(i, n))
        n = len(arr)
        @lru_cache(None)
        def solve(i, j):
            if j - i <= 1:
                return 0
            return min([max(arr[i:k])*max(arr[k:j])+solve(i,k)+solve(k,j)
                        for k in range(i+1,j)])
        return solve(0, n)

