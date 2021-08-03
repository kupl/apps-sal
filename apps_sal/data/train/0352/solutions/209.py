class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        n = len(words)
        words = [(len(word), word) for word in words]
        words.sort()
        words = [word[1] for word in words]
        dp = [1 for i in range(n)]

        for i in range(n):
            for j in reversed(list(range(i))):
                if len(words[j]) < len(words[i]) - 1:
                    break

                if len(words[j]) == len(words[i]):
                    continue

                if self.check(words[j], words[i]):
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

    def check(self, s1, s2):
        i, j = 0, 0
        count = 0
        while i < len(s1) and j < len(s2):
            if s1[i] == s2[j]:
                i += 1
                j += 1
            else:
                j += 1
                count += 1

        return i == len(s1)
