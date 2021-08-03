class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        def is_pred(short, long):
            if len(short) + 1 != len(long):
                return False
            short += ' '
            new = None
            for i in range(len(long)):
                if short[i] != long[i]:
                    new = i
                    break
            if short[:-1] == long[:new] + long[(new + 1):]:
                return True
            return False
        words.sort(key=lambda x: len(x))
        dp = [1] * len(words)
        for i in range(1, len(words)):
            for j in range(i):
                if is_pred(words[j], words[i]):
                    if dp[j] >= dp[i]:
                        dp[i] = dp[j] + 1
        return max(dp)
