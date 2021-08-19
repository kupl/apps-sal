class Solution:

    def longestStrChain(self, words: List[str]) -> int:
        N = len(words)
        if N < 2:
            return N
        words.sort(key=len)
        Table = {word: 1 for word in words}
        result = 1
        for word in words:
            for j in range(len(word)):
                subword = word[:j] + word[j + 1:]
                if subword in Table and Table[subword] >= Table[word]:
                    Table[word] = Table[subword] + 1
            if Table[word] > result:
                result = Table[word]
        return result
