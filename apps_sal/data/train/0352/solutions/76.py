class Solution:

    def longestStrChain(self, words: List[str]) -> int:
        m = collections.defaultdict(list)
        for w in words:
            m[len(w)].append(w)
        if len(m) == 1:
            return 1
        for k in list(m.keys()):
            m[k] = [''.join(sorted(x)) for x in m[k]]

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
        return max((dfs(x) for y in sorted(list(m.keys()))[:-1] for x in m[y])) + 1
