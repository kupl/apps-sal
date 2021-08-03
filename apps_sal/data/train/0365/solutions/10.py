class Solution:
    def uniqueLetterString(self, s: str) -> int:
        n = len(s)
        mod = 10**9 + 7
        index = defaultdict(deque)
        for i, c in enumerate(s):
            index[c].append(i)
        for c in index:
            index[c].append(n)
            index[c].appendleft(-1)
        ans = 0
        for c in list(index.keys()):
            for i in range(1, len(index[c]) - 1):
                ans = (ans + (index[c][i] - index[c][i - 1]) * (index[c][i + 1] - index[c][i])) % mod

        return ans
