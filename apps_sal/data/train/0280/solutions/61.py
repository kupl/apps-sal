def ch(a):
    l = len(a)
    c = 0
    for i in range(l // 2):
        c += a[i] != a[l - i - 1]
    return c


def f(s, ci, k, d):
    l = len(s)
    if k == 0:
        if ci != l:
            return math.inf
        return 0
    if ci == l:
        return math.inf
    if d[ci][k] != -1:
        return d[ci][k]
    r = ''
    a = math.inf
    for i in range(ci, l):
        r += s[i]
        a = min(ch(s[ci:i + 1]) + f(s, i + 1, k - 1, d), a)
    d[ci][k] = a
    return a


class Solution:

    def palindromePartition(self, s: str, k: int) -> int:
        l = len(s)
        d = [[-1 for i in range(k + 1)] for j in range(l)]
        return f(s, 0, k, d)
