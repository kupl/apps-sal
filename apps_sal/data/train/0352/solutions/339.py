class Solution:

    def longestStrChain(self, words: List[str]) -> int:
        d = {j: 1 for j in words}
        n = len(words)
        used = {}
        c = [0]
        words = sorted(words, key=len)

        def dfs(s, l):
            if not s or s not in d:
                c[0] = max(c[0], len(l))
                return
            used[s] = 1
            m = 0
            for i in range(len(s)):
                dfs(s[:i] + s[i + 1:], l + [s])
                m = max(m, len(l))
        for i in range(n - 1, -1, -1):
            if words[i] not in used and c[0] < i:
                dfs(words[i], [])
        return c[0]
