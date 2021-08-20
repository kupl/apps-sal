class Solution:
    _max = 0

    def longestStrChain(self, words: List[str]) -> int:

        def dfs(cur, step):
            if cur not in s:
                return
            if len(cur) == 0:
                return
            self._max = max(step, self._max)
            for i in range(len(cur)):
                t = cur[:i] + cur[i + 1:]
                dfs(t, step + 1)
        s = set(words)
        for w in sorted(words, key=len, reverse=True):
            dfs(w, 1)
        return self._max
