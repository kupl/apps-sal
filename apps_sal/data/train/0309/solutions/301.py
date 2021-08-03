class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        seen = set()
        dp = [defaultdict(int) for _ in range(len(A))]
        mx = 0

        for i in range(len(A)):
            seen.add(A[i])
            for j in range(0, i):
                ap = A[i] + -A[j]

                if A[i] + -ap in seen:
                    dp[i][ap] = dp[j][ap] + 1
                    mx = max(mx, dp[i][ap])

        return mx + 1
