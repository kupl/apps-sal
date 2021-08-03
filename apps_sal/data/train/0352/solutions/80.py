class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        def isPred(w1, w2):
            i, j = 0, 0
            while i < len(w1):
                if w1[i] != w2[j]:
                    if j != i:
                        return False
                    j += 1
                else:
                    j += 1
                    i += 1
            return True

        words = sorted(words, key=lambda x: len(x))
        dp = [1] * len(words)
        for i in range(1, len(words)):
            for j in range(i):
                if len(words[i]) == (len(words[j]) + 1) and isPred(words[j], words[i]):
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)
