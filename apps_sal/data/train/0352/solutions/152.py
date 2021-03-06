class Solution:

    def longestStrChain(self, words: List[str]) -> int:
        if not words:
            return 0
        words.sort(key=lambda x: len(x))
        visited = set()
        res = 1
        for i in range(len(words)):
            if words[i] in visited:
                continue
            visited.add(words[i])
            res = max(res, self.dfs(words, words[i], i + 1, visited))
        return res

    def dfs(self, words, cur, start, visited):
        if start >= len(words):
            return 1
        ma = 1
        for i in range(start, len(words)):
            if len(words[i]) > len(cur) + 1:
                break
            if len(words[i]) == len(cur):
                continue
            if not self.isPredecessor(cur, words[i]):
                continue
            visited.add(words[i])
            ma = max(ma, 1 + self.dfs(words, words[i], i + 1, visited))
        return ma

    def isPredecessor(self, w1, w2):
        for i in range(len(w1)):
            if w1[:i] == w2[:i] and w1[i:] == w2[i + 1:]:
                return True
        if w1 == w2[:-1]:
            return True
        return False
