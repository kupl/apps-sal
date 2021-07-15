class Solution:
    def isPredecessor(self, word1, word2):
        if len(word1)+1 == len(word2):
            i = 0
            j = 0
            count = 0
            while i < len(word1) and j < len(word2):
                if word1[i] != word2[j]:
                    count += 1
                else:
                    i += 1
                j += 1
            if count > 1:
                return False
            elif count == 0:
                if len(word2) == j + 1:
                    return True
            else:
                return True
        else:
            return False
        
    def memoization(self, i, words, memo):
        if i >= len(words):
            return 0
        if memo[i] is not None:
            return memo[i]
        length = 0
        for j in range(i+1, len(words)):
            # if i==14:
            #     print(words[i], words[j], self.isPredecessor(words[i], words[j]))
            if self.isPredecessor(words[i], words[j]):
                length = max(length, self.memoization(j, words, memo))
        memo[i] = 1 + length
        return memo[i]

    def longestStrChain(self, words: List[str]) -> int:
        words = sorted(words, key=len)
        memo = [None]*len(words)
        length = 0
        for i in range(len(words)):
            length = max(length, self.memoization(i, words, memo))
        return length
