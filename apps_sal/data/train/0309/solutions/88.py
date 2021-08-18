from heapq import heappop, heapify


class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:

        count = 0

        dp = defaultdict(lambda: defaultdict(int))

        for i in range(1, len(A)):
            seen = set()
            for j in range(i - 1, -1, -1):
                diff = A[i] - A[j]
                if diff not in seen:
                    dp[i][diff] += dp[j][diff] + 1
                    count = max(count, dp[i][diff])
                    seen.add(diff)

        return count + 1
