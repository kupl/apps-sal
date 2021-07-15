class Solution:
    def longestStrChain(self, words: List[str]) -> int:
                # contruct a graph linking predecessor
        def isPred(word1, word2):
            # len(word2) > len(word1)
            for i in range(len(word2)):
                if word2[0:i] + word2[i+1:] == word1:
                    return True
            return False
        graph = {}
        for i in range(len(words) - 1):
            for j in range(i + 1, len(words)):
                w1, w2 = words[i], words[j]
                if len(w2) - len(w1) == 1 and isPred(w1, w2):
                    if w1 in graph:
                        graph[w1].append(w2)
                    else:
                        graph[w1] = [w2]
                elif len(w2) - len(w1) == -1 and isPred(w2, w1):
                    if w2 in graph:
                        graph[w2].append(w1)
                    else:
                        graph[w2] = [w1]
        self.res = 0
        def dfs(word, lev):
            # no need to mark visited here as len goes up
            self.res = max(self.res, lev)
            if word not in graph:
                return
            for i in graph[word]:
                dfs(i, lev+1)
        for i_word in words:
            dfs(i_word, 1)
        return self.res
