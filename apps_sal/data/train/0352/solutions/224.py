class Solution:

    def longestStrChain(self, words: List[str]) -> int:
        sort = [[] for _ in range(max(map(len, words)))]
        for el in words:
            sort[len(el) - 1].append(el)
        d = collections.defaultdict(int)
        for row in sort:
            for w in row:
                for i in range(len(w)):
                    l = w[:i] + w[i + 1:]
                    t = d[l] + 1
                    d[w] = max(d[w], t)
        return max(d.values())
