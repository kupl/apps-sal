class Solution:

    def lenLongestFibSubseq(self, A: List[int]) -> int:
        dp = {}
        s = set(A)
        for (j, c) in enumerate(A):
            for b in A[:j]:
                a = c - b
                if a < b and a in s:
                    dp[b, c] = dp.get((a, b), 2) + 1
        return max(dp.values() or [0])
