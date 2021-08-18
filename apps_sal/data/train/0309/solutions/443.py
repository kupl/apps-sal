class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        from collections import Counter, defaultdict

        min_val = min(A)
        max_val = max(A)

        global_best = -1
        dp = {}
        prev = defaultdict(list)

        for i, v in enumerate(A):
            dp[i] = {}

            for d in range(min_val - v, max_val - v + 1):
                if v + d < min_val or v + d > max_val:
                    raise Exception()

                best = 0

                if v + d in prev:
                    for j in prev[v + d]:
                        best = max(best, dp[j].get(d, 1))

                dp[i][d] = best + 1
                global_best = max(global_best, dp[i][d])

            prev[v].append(i)

        return global_best
