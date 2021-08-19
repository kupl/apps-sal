class Solution:

    def longestStrChain(self, words: List[str]) -> int:
        if len(words) == 0:
            return False
        words.sort(key=lambda x: len(x))

        def check(a, b):
            for i in range(len(b) - 1):
                if a[i] != b[i]:
                    return b[i + 1:] == a[i:]
            return True
        ans = 1
        dp = [1] * len(words)
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if len(words[j]) > 1 + len(words[i]):
                    break
                if len(words[j]) == 1 + len(words[i]):
                    if check(words[i], words[j]):
                        dp[j] = max(dp[j], 1 + dp[i])
                        ans = max(ans, dp[j])
        return ans
