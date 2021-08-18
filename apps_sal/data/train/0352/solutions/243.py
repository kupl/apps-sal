class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        N = len(words)
        dp = [1] * N
        words.sort(key=len)
        print(words)
        if N == 1:
            return 1

        def check(word1, word2):
            if len(word2) - len(word1) != 1:
                return False
            n = len(word1)
            for i in range(n):
                if word2[:i] + word2[i + 1:] == word1:
                    return True
                if word2[:-1] == word1:
                    return True
            return False

        for i in range(N):
            for j in range(i):
                if check(words[j], words[i]):
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)
