from collections import Counter
_MODER = 998244353


def solve(n, a):
    r = 0
    c = Counter()
    for e in a:
        c[len(str(e))] += 1
    for e in a:
        s = str(e)
        current_len = len(s)
        for (k, v) in list(c.items()):
            if k >= current_len:
                ns = '0'.join(list(s)) + '0'
            else:
                ns = s[:current_len - k] + '0'.join(list(s[current_len - k:])) + '0'
            r = (r + int(ns) * v % _MODER) % _MODER
            if k >= current_len - 1:
                ns = '0'.join(list(s))
            else:
                ns = s[:current_len - k - 1] + '0'.join(list(s[current_len - k - 1:]))
            r = (r + int(ns) * v % _MODER) % _MODER
    return r


n = int(input())
a = list(map(int, input().split()))
r = solve(n, a)
print(r)
