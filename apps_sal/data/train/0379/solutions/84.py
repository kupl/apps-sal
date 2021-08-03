class Solution:
    def maxSum(self, A: List[int], B: List[int]) -> int:

        g = collections.defaultdict(list)

        for i in range(len(A) - 1):
            g[A[i]].append(A[i + 1])
        for i in range(len(B) - 1):
            g[B[i]].append(B[i + 1])

        g[A[-1]]
        g[B[-1]]

        dp = collections.defaultdict(int)

        for node in sorted(g, reverse=True):

            dp[node] = node
            if g[node]:
                dp[node] += max(dp[nei] for nei in g[node])

        return max(dp.values()) % (10**9 + 7)
