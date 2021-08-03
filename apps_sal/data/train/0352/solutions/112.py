class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        def ispre(w1, w2):
            i, j = 0, 0
            while i < len(w1) and j < len(w2):
                if w1[i] == w2[j]:
                    i += 1
                    j += 1
                else:
                    j += 1
            return i == len(w1)

        words.sort(key=len)
        dp = [0] * len(words)

        def dfs(i):
            if dp[i] != 0:
                return dp[i]
            dp[i] = 1
            for j in range(i, len(words)):
                if len(words[j]) <= len(words[i]):
                    continue
                if len(words[j]) > len(words[i]) + 1:
                    break
                if ispre(words[i], words[j]):
                    dp[i] = max(dp[i], 1 + dfs(j))
            return dp[i]

        ans = max(dfs(i) for i in range(len(words)))
        return ans
