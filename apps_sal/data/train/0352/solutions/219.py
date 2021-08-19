class Solution:

    def longestStrChain(self, words: List[str]) -> int:

        def helper(word_pre, word_cur):
            if len(word_pre) - len(word_cur) != -1:
                return False
            (count, pre, cur) = (0, 0, 0)
            while pre <= len(word_pre) and cur < len(word_cur):
                if pre < len(word_pre) and word_cur[cur] == word_pre[pre]:
                    pre += 1
                else:
                    count += 1
                cur += 1
            return True if count == 1 else False
        dp = [1] * len(words)
        words = sorted(words, key=len)
        for i in range(len(words)):
            for j in range(i):
                if helper(words[j], words[i]) and dp[j] > dp[i] - 1:
                    dp[i] = dp[j] + 1
        return max(dp)
