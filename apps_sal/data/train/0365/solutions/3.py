class Solution:
    def uniqueLetterString(self, s: str) -> int:
        n = len(s)
        dbefore = {}
        dafter = {}
        before = [-1] * n
        after = [n] * n
        for i in range(n):
            before[i] = dbefore.get(s[i], -1)
            after[n - 1 - i] = dafter.get(s[n - 1 - i], n)
            dbefore[s[i]] = i
            dafter[s[n - 1 - i]] = n - 1 - i
        c = 10 ** 9 + 7
        res = 0
        for i in range(n):
            res += (i - before[i]) * (after[i] - i)
            res %= c
        return res
