import collections


def f():
    n, m = [int(c) for c in input().split()]

    r = []
    for i in range(m):
        a = [int(c) for c in input().split()]
        jj = a.index(max(a)) + 1
        r.append(jj)

    c = collections.Counter(r)
    mm = 0
    for k in c:
        if c[k] > mm:
            mm = c[k]

    for k in sorted(c.keys()):
        if c[k] == mm:
            return k


print(f())
