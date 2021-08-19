class Solution:

    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=lambda x: len(x), reverse=True)
        minLen = len(words[-1])
        dic = set(words)
        seen = set()
        self.result = 0
        for word in words:
            if word not in seen:
                length = 1
                self.dfs(word, dic, seen, minLen, length)
        return self.result

    def dfs(self, word, dic, seen, minLen, length):
        self.result = max(self.result, length)
        if len(word) == minLen:
            return
        seen.add(word)
        for i in range(len(word)):
            new = word[:i] + word[i + 1:]
            if new in dic:
                self.dfs(new, dic, seen, minLen, length + 1)
