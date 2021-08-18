import collections


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        self.graph = collections.defaultdict(list)

        for word in words:
            self.graph[len(word)].append(word)

        for word1 in words:
            for word2 in self.graph[len(word1) + 1]:
                for i in range(len(word2)):
                    if word2[:i] + word2[i + 1:] == word1:
                        self.graph[word1].append(word2)

        return max(self.dfs(w, 1) for w in words)

    def dfs(self, word1, size):
        return max([self.dfs(word2, size + 1) for word2 in self.graph[word1]], default=size)
