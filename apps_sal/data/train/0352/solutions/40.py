class Solution:
    def isPredecessor(self, word1, word2):
        for i in range(1, len(word2) + 1):
            if (word2[:i - 1] + word2[i:]) == word1:
                return True
        return False

    def longestStrChain(self, words: List[str]) -> int:
        wordLengths = {}
        for word in words:
            if len(word) in wordLengths:
                wordLengths[len(word)].append(word)
            else:
                wordLengths[len(word)] = [word]
        longestStrChains = {}
        totalMaxLength = 1
        for length in sorted(wordLengths.keys()):
            for word in wordLengths[length]:
                if len(word) - 1 not in wordLengths:
                    longestStrChains[word] = 1
                else:
                    maxLength = 1
                    for smallerWord in wordLengths[len(word) - 1]:
                        if self.isPredecessor(smallerWord, word):
                            if maxLength < longestStrChains[smallerWord] + 1:
                                maxLength = longestStrChains[smallerWord] + 1
                    longestStrChains[word] = maxLength
                    if totalMaxLength < maxLength:
                        totalMaxLength = maxLength
        print(wordLengths)
        print(longestStrChains)
        return totalMaxLength
