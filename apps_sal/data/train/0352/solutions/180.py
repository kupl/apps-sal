class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words = sorted(words, key=lambda w: len(w))
        dp = [None] * len(words)
        dp[0] = 1
        for i in range(1, len(words)):
            maxi = 1
            for j in list(range(0, i))[::-1]:
                if(self.check(words[j], words[i]) and dp[j] + 1 > maxi):
                    maxi = dp[j] + 1
            dp[i] = maxi
        return max(dp)

    def check(self, chain, word):
        if(len(chain) + 1 != len(word)):
            return False
        i = 0
        j = 0
        Flag = False
        while(i < len(chain) and j < len(word)):
            if(chain[i] == word[j]):
                i += 1
                j += 1
            elif(chain[i] != word[j] and not Flag):
                j += 1
                Flag = True
            else:
                return False
        return True
