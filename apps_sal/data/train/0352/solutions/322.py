class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        graph = {}
        max_dist = 0
        for word in words:
            length = len(word)
            dist = 0
            for i in range(length):
                if (check := word[:i] + word[i + 1:]) in graph:
                    dist = max(graph[check], dist)
                graph[word] = dist + 1
                max_dist = max(max_dist, graph[word])
        return max_dist
