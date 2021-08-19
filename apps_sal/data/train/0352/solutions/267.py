class Solution:

    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=lambda x: len(x))
        wordLevels = {}
        for word in words:
            if len(word) in wordLevels:
                wordLevels[len(word)].append(word)
            else:
                wordLevels[len(word)] = [word]
        result = 0
        words.reverse()
        for word in words:
            result = max(result, self.getChain(word, wordLevels, 1))
        return result

    def getChain(self, word, wordLevels, length):
        level = len(word)
        for i in range(len(word)):
            if level - 1 in wordLevels:
                if word[:i] + word[i + 1:] in wordLevels[level - 1]:
                    return self.getChain(word[:i] + word[i + 1:], wordLevels, length + 1)
        return length
