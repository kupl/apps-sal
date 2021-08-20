class Solution:

    def lenLongestFibSubseq(self, A: List[int]) -> int:
        n = len(A)
        dp = [[2] * n for _ in range(n)]
        loc = {A[0]: 0, A[1]: 1}
        longest = 0
        for k in range(2, n):
            loc[A[k]] = k
            for j in range(k):
                target = A[k] - A[j]
                if target in loc and loc[target] < j:
                    dp[j][k] = dp[loc[target]][j] + 1
                    longest = max(longest, dp[j][k])
        return longest
        'dp = {}\n        dp[(A[1], A[0] + A[1])] = 2\n        for i in range(2, len(A)):\n            for j in range(i):\n                if (A[j], A[i]) not in dp:\n                    dp[(A[i], A[j] + A[i])] = 2\n                else:\n                    dp[(A[i], A[j] + A[i])] = dp[(A[j], A[i])] + 1\n                    del dp[(A[j], A[i])]\n        longest = max(dp.values())\n        \n        return longest if longest > 2 else 0'
