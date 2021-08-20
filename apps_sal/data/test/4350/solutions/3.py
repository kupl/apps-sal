import sys
from math import *


def minp():
    return sys.stdin.readline().strip()


def mint():
    return int(minp())


def mints():
    return map(int, minp().split())


def main():
    (n, m) = mints()
    res = []
    a = [None] * n
    l = [None] * n
    r = [None] * n
    s = [0] * n
    for i in range(n):
        a[i] = list(minp())
        l[i] = [i for i in range(m)]
        r[i] = [i for i in range(m)]
        s[i] = [0] * m
    for i in range(n):
        j = 0
        b = a[i]
        ll = l[i]
        rr = r[i]
        while j < m:
            if b[j] == '*':
                jj = j + 1
                while jj < m and b[jj] == '*':
                    jj += 1
                jj -= 1
                for k in range(j, jj + 1):
                    ll[k] = j
                    rr[k] = jj
                j = jj + 1
            else:
                j += 1
    for i in range(m):
        j = 0
        while j < n:
            if a[j][i] == '*':
                jj = j + 1
                while jj < n and a[jj][i] == '*':
                    jj += 1
                jj -= 1
                for k in range(j, jj + 1):
                    x = min(i - l[k][i], r[k][i] - i, k - j, jj - k)
                    s[k][i] = x
                    if x > 0:
                        res.append((k + 1, i + 1, x))
                j = jj + 1
            else:
                j += 1
    for i in range(n):
        j = 0
        ss = s[i]
        rr = r[i]
        c = -1
        while j < m:
            if ss[j] > 0 and c < ss[j]:
                c = ss[j]
            if c >= 0:
                rr[j] = '*'
            else:
                rr[j] = '.'
            j += 1
            c -= 1
        j = m - 1
        c = -1
        while j >= 0:
            if ss[j] > 0 and c < ss[j]:
                c = ss[j]
            if c >= 0:
                rr[j] = '*'
            c -= 1
            j -= 1
    for i in range(m):
        j = 0
        c = -1
        while j < n:
            x = s[j][i]
            if x > 0 and c < x:
                c = x
            if c >= 0:
                r[j][i] = '*'
            j += 1
            c -= 1
        j = n - 1
        c = -1
        while j >= 0:
            x = s[j][i]
            if x > 0 and c < x:
                c = x
            if c >= 0:
                r[j][i] = '*'
            if r[j][i] != a[j][i]:
                print(-1)
                return
            c -= 1
            j -= 1
    print(len(res))
    for i in res:
        print(*i)


main()
