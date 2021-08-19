class Solution:

    def uniqueLetterString(self, s: str) -> int:
        index = collections.defaultdict(list)
        for (i, c) in enumerate(s):
            index[c].append(i)
        ans = 0
        for a in index.values():
            a = [-1] + a + [len(s)]
            for i in range(1, len(a) - 1):
                ans += (a[i] - a[i - 1]) * (a[i + 1] - a[i])
        return ans % (10 ** 9 + 7)
