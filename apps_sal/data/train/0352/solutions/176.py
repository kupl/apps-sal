class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp = {}
        result = 1

        for word in sorted(words, key=lambda x: -len(x)):
            dp[word] = 1

            for i in range(len(word)+1):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = word[:i] + c + word[i:]

                    if next_word in dp:
                        dp[word] = max(dp[word], dp[next_word] + 1)
                        result = max(result, dp[word])

        return result
