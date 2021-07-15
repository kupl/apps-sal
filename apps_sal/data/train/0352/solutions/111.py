class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        if not words:
            return 0
        words = sorted(words, key=lambda x: len(x))
        print(words)
        def valid(word1, word2):
            i = 0
            j = 0
            flag = False
            while i < len(word1) and j < len(word2):
                if word1[i] == word2[j]:
                    i += 1
                    j += 1
                    continue
                if not flag and word1[i] != word2[j]:
                    flag = True
                    j += 1
                    continue
                if flag and word1[i] != word2[j]:
                    return False
            
            return i == len(word1)
                
        
        res = 1
        dp = [1] * len(words)
        for i in range(1, len(words)):
            for j in range(i):
                if len(words[j]) + 1 == len(words[i]) and valid(words[j], words[i]):
                    dp[i] = max(dp[i], dp[j]+1)
            res = max(res, dp[i])
        # print(dp)
        return res
