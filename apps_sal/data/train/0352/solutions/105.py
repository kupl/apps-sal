class Solution:
    def longestStrChain(self, words: List[str]) -> int:

        if not words:
            return 0

        words = sorted(words, key=lambda x: len(x))

        dp = [1] * len(words)

        for i in range(1, len(words)):

            for j in range(i - 1, -1, -1):

                if len(words[i]) == len(words[j]) + 1:

                    update = True

                    for c in words[j]:
                        if c not in words[i]:
                            update = False

                    if update:
                        dp[i] = max(dp[i], 1 + dp[j])

        return max(dp)
