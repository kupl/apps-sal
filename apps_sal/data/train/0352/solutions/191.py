class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp = [0] * len(words)

        words.sort(key=lambda x: len(x))

        def predecessor(a, b):
            if len(a) == len(b):
                return False
            diff = 0
            i = 0
            j = 0
            while i < len(a) and j < len(b):
                if a[i] != b[j]:
                    diff += 1
                    if diff >= 2:
                        return False
                    i += 1
                else:
                    i += 1
                    j += 1
            return True
        for i, word in enumerate(words):
            dp[i] = 1
            for j in range(i - 1, -1, -1):
                if len(words[i]) - len(words[j]) >= 2:
                    break
                if predecessor(words[i], words[j]):
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
