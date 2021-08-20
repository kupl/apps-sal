class Solution:

    def longestStrChain(self, words: List[str]) -> int:
        children = collections.defaultdict(set)
        for i in range(len(words)):
            for j in range(len(words)):
                if len(words[i]) == len(words[j]) + 1:
                    for k in range(len(words[i])):
                        if words[i][:k] + words[i][k + 1:] == words[j]:
                            children[words[j]].add(words[i])
        print(children)

        def dfs(w, count):
            visited.add(w)
            if not children[w]:
                self.res = max(self.res, count)
            else:
                for v in children[w]:
                    dfs(v, count + 1)
        visited = set()
        self.res = 0
        for u in words:
            if u not in visited:
                dfs(u, 1)
        return self.res
