class Solution:

    def lenLongestFibSubseq(self, A: List[int]) -> int:
        from collections import defaultdict
        ans = 0
        mapA = {n: i for (i, n) in enumerate(A)}
        dp = defaultdict(lambda: 2)
        for (k, z) in enumerate(A):
            for j in range(k):
                i = mapA.get(z - A[j])
                if i is not None and i < j:
                    temp = dp[j, k] = dp[i, j] + 1
                    ans = max(ans, temp)
        return ans if ans >= 3 else 0
