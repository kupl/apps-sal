class Solution:

    def longestStrChain(self, words: List[str]) -> int:

        def pred(a, b):
            if len(a) == len(b) or len(a) - len(b) > 1:
                return False
            diff = 0
            i = 0
            j = 0
            while i < len(a):
                if a[i] == b[j]:
                    i += 1
                    j += 1
                else:
                    diff += 1
                    if diff > 1:
                        return False
                    j += 1
            return True
        if not words:
            return 0
        dp = [0 for w in words]
        ret = 0
        words.sort(key=len)
        for i in range(len(words)):
            dp[i] = 1
            for j in range(i):
                if len(words[i]) - len(words[j]) <= 1 and pred(words[j], words[i]):
                    dp[i] = max(dp[i], dp[j] + 1)
            ret = max(ret, dp[i])
        return ret
