class Solution:

    def longestStrChain(self, words: List[str]) -> int:
        d = {}
        for word in words:
            if len(word) in d:
                d[len(word)].append(word)
            else:
                d[len(word)] = [word]
        visited = {}
        res = 0
        for word in sorted(words):
            res = max(res, self.dfs(word, visited, d))
        return res

    def checkPredecessor(self, word1, word2):
        return any((word1 == word2[:i] + word2[i + 1:] for i in range(len(word2))))

    def dfs(self, word, visited, d):
        if word in visited:
            return visited[word]
        if len(word) + 1 not in d:
            visited[word] = 1
            return 1
        res = 1
        for w in d[len(word) + 1]:
            if self.checkPredecessor(word, w):
                res = max(res, self.dfs(w, visited, d) + 1)
        visited[word] = res
        return res
