class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = [dict() for a in A]
        for (idx, a) in enumerate(A):
            for j in range(idx):
                diff = a - A[j]
                dp[idx][diff] = dp[j].get(diff, 1) + 1

        def get_len(d):
            if not d:
                return 0
            return max(d.values())
        return max(map(get_len, dp))
