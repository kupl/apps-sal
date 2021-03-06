class Solution:

    def longestStrChain(self, words: List[str]) -> int:
        wset = set(words)
        memo = {}

        def dp(word):
            if word in memo:
                return memo[word]
            ans = 1
            for i in range(len(word) + 1):
                for j in range(26):
                    newword = word[:i] + chr(ord('a') + j) + word[i:]
                    if newword in wset:
                        ans = max(ans, 1 + dp(newword))
            memo[word] = ans
            return ans
        ret = 0
        for word in words:
            if not word in memo:
                ret = max(ret, dp(word))
        return ret
