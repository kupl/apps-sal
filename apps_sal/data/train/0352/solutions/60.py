class Solution:

    def longestStrChain(self, words: List[str]) -> int:
        dp = {}
        words_dict = {}
        for word in words:
            dp[word] = -1
            if words_dict.get(len(word)):
                words_dict[len(word)].append(word)
            else:
                words_dict[len(word)] = [word]
        result = 0
        for word in words:
            result = max(result, self.longest_chain(word, dp, words_dict))
        return result

    def longest_chain(self, word, dp, words_dict):
        if dp[word] != -1:
            return dp[word]
        if not words_dict.get(len(word) + 1):
            return 1
        res = 0
        for word2 in words_dict[len(word) + 1]:
            if self.isSucc(word, word2):
                res = max(res, self.longest_chain(word2, dp, words_dict))
        res += 1
        return res

    def isSucc(self, word1, word2):
        if len(word1) != len(word2) - 1:
            return False
        count = 0
        i = 0
        j = 0
        while i < len(word1):
            if word1[i] != word2[j]:
                if count == 1:
                    return False
                count += 1
                j += 1
            else:
                j += 1
                i += 1
        return True
