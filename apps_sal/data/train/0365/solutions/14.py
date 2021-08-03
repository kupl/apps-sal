class Solution:
    def uniqueLetterString(self, s: str) -> int:
        if not s:
            return 0

        dp = collections.defaultdict(list)
        for index, val in enumerate(s):
            dp[val].append(index)

        ans = 0
        for A in list(dp.values()):
            A = [-1] + A + [len(s)]

            for i in range(1, len(A) - 1):
                ans += (A[i] - A[i - 1]) * (A[i + 1] - A[i])

        return ans % (10**9 + 7)
