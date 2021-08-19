class Solution:

    def longestStrChain(self, words: List[str]) -> int:
        n = len(words)
        W = defaultdict(list)
        for (i, w) in enumerate(words):
            W[len(w)].append(i)
        G = defaultdict(set)
        for i in range(n):
            for j in W[len(words[i]) + 1]:
                found = False
                for k in range(len(words[j])):
                    if words[i] == words[j][:k] + words[j][k + 1:]:
                        found = True
                        break
                if found:
                    G[i].add(j)

        @lru_cache(None)
        def dfs(i):
            out = 1
            for j in G[i]:
                out = max(out, 1 + dfs(j))
            return out
        return max((dfs(i) for i in range(n)))
