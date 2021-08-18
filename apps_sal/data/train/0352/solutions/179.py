class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words = sorted(words, key=lambda word: len(word))
        n = len(words)
        if n == 1:
            return 1

        ans = 1
        dp = [1] * n

        def match(i, j):
            idx_i = 0
            idx_j = 0
            skipped = False
            while idx_j < len(words[j]):
                if words[i][idx_i] != words[j][idx_j]:
                    if skipped:
                        return False
                    skipped = True
                    idx_i += 1
                else:
                    idx_i += 1
                    idx_j += 1
            return True

        for i in range(1, n):
            for j in range(i - 1, -1, -1):
                if len(words[i]) - len(words[j]) > 1:
                    break
                elif len(words[i]) - len(words[j]) == 1:
                    if match(i, j):
                        dp[i] = max(dp[i], dp[j] + 1)
                        ans = max(ans, dp[i])
                else:
                    pass

        return ans
