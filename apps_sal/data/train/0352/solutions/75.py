class Solution:

    def longestStrChain(self, words: List[str]) -> int:
        n = len(words)
        a = sorted(words, key=len)
        dp = [1] * n

        def helper(a1, b1):
            s = 0
            n = len(b1)
            i = 0
            j = 0
            while i < n and j < n + 1:
                if a1[j] == b1[i]:
                    i += 1
                    j += 1
                elif a1[j] != b1[i] and s == 0:
                    s += 1
                    j += 1
                else:
                    return 0
            return 1
        for i in range(1, n):
            for j in range(i - 1, -1, -1):
                if len(a[j]) == len(a[i]):
                    continue
                elif len(a[j]) < len(a[i]) - 1:
                    break
                x = helper(a[i], a[j])
                if x == 1:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
