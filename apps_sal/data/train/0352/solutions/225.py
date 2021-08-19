class Solution:

    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        N = len(words)
        self.longest = [None] * N
        max_len = 1
        for i in range(N):
            max_len = max(max_len, self.__findLongestAfter(words, i))
        return max_len

    def __isPredecessor(self, w1, w2):
        if len(w2) != len(w1) + 1:
            return False
        i = j = 0
        while i < len(w1) and j < len(w2):
            if w1[i] == w2[j]:
                i += 1
            j += 1
        return i == len(w1)

    def __findLongestAfter(self, words: List[str], i: int) -> int:
        if self.longest[i] is not None:
            return self.longest[i]
        self.longest[i] = 1
        len_i = len(words[i])
        for j in range(i + 1, len(words)):
            if len(words[j]) > len_i + 1:
                break
            if self.__isPredecessor(words[i], words[j]):
                self.longest[i] = max(self.longest[i], self.__findLongestAfter(words, j) + 1)
        return self.longest[i]
