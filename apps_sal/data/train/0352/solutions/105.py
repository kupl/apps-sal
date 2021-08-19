class Solution:
    def longestStrChain(self, words: List[str]) -> int:

        if not words:
            return 0

        # O(n log n)
        words = sorted(words, key=lambda x: len(x))

        # O(n) space
        dp = [1] * len(words)

        # O(n^2)
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
