class Solution:
    def minDifficulty(self, A: List[int], d: int) -> int:
        n = len(A)
        if(n < d):
            return -1

        @lru_cache(None)
        def helper(i, d):
            if(d == 0):
                return 0 if i == n else sum(A[i:])

            if(i == n):
                return float('inf')
            tmp = 0
            ans = float('inf')
            for j in range(i, n):
                tmp = max(tmp, A[j])
                ans = min(ans, tmp + helper(j + 1, d - 1))
            return ans
        return helper(0, d)
