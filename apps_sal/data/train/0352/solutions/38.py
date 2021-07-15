
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=lambda x: len(x))
        print(words)
        if not words:
            return 0
            
        max_chain_dp = {}
        max_len = 1
        for i in range(len(words)):
            word_len = len(words[i])
            max_chain_dp[words[i]] = 1
            for j in range(i-1, -1, -1):
                if len(words[j]) == word_len:
                    continue
                elif len(words[j]) + 1 == word_len:
                    if self.isChain(words[j], words[i]):
                        max_chain_dp[words[i]] = max(1 + max_chain_dp[words[j]], max_chain_dp[words[i]])
                        max_len = max(max_chain_dp[words[i]], max_len)
                else:
                    break
        return max_len
                
                
    def isChain(self, word1, word2):
        if len(word2) - len(word1) > 1:
            return False
        added = False
        i, j = 0, 0
        while i < len(word1) or j < len(word2):
            if i < len(word1) and word1[i] == word2[j]:
                i += 1
                j += 1
            else:
                if added:
                    return False
                else:
                    j += 1
                    added = True

        if i == len(word1) and j == len(word2):
            return True


                

