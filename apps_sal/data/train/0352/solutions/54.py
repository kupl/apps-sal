class Solution:

    def longestStrChain(self, words: List[str]) -> int:
        m = collections.defaultdict(list)
        words = sorted(words, key=len)
        for w in words:
            m[len(w)].append(''.join(sorted(w)))
        if len(m) == 1:
            return 1

        def equal(x, y):
            for i in range(len(x)):
                if x[i] != y[i]:
                    return x == y[:i] + y[i + 1:]
            return True

        def dfs(w):
            k = len(w) + 1
            if k not in m:
                return 0
            return max([dfs(x) + 1 for x in m[k] if equal(w, x)] or [0])
        return max((dfs(x) for y in list(m.keys())[:-1] for x in m[y])) + 1
