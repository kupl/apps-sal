class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        indexes = {n: i for i, n in enumerate(A)}
        dp, ans = collections.defaultdict(lambda: 2), 0

        for i, n in enumerate(A):
            for j in range(i):
                idx = indexes.get(n - A[j], None)
                if idx is not None and idx < j:
                    cand = dp[j, i] = dp[idx, j] + 1
                    ans = max(ans, cand)
        return ans if ans >= 3 else 0
