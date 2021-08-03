class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        def check(str1, str2):
            for i in range(len(str2)):
                temp = str2[:i] + str2[i + 1:]
                if temp == str1:
                    return True
            return False
        words.sort(key=len)
        min_length = len(words[0])
        dp = [1] * len(words)

        for i in range(len(words)):
            if len(words[i]) == min_length:
                continue
            for j in range(len(words)):
                if len(words[j]) == len(words[i]) - 1:
                    if check(words[j], words[i]):
                        dp[i] = max(dp[i], dp[j] + 1)
                elif len(words[j]) >= len(words[i]):
                    break
        return max(dp)
