class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        n = len(words)
        dp = [1] * n
        for i in range(n):
            for j in reversed(list(range(i))):
                if len(words[i]) == len(words[j]):
                    continue
                elif len(words[i]) > len(words[j]) + 1:
                    break

                if self.helper(words[j], words[i]):
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

    def helper(self, w1, w2):
        i = 0
        while i < len(w1) and w1[i] == w2[i]:
            i += 1

        while i < len(w1) and w1[i] == w2[i + 1]:
            i += 1

        return i == len(w1)
