
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        wordCounter = [collections.Counter(x) for x in words]
        dp = [1 for _ in range(len(words))]
        for i in range(len(words) - 2, -1, -1):
            for j in range(i + 1, len(words)):
                if len(words[i]) == len(words[j]):
                    continue
                if len(words[j]) - len(words[i]) > 1:
                    break
                if len(wordCounter[j] - wordCounter[i]) == 1:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
