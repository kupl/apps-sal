import collections
import bisect


def f():
    (n, m) = [int(c) for c in input().split()]
    s = list(input())
    ll = []
    start = 0
    length = 0
    inside = False
    cc = 0
    for i in range(len(s)):
        if s[i] == '.':
            if not inside:
                inside = True
            length += 1
        elif inside:
            cc += length - 1
            length = 0
            inside = False
    if inside:
        cc += length - 1
    res = [0] * m
    for i in range(m):
        line = input().split()
        j = int(line[0]) - 1
        c = line[1]
        if c == '.' and s[j] == '.' or (c != '.' and s[j] != '.'):
            res[i] = cc
        else:
            e1 = False
            e2 = False
            if j > 0 and s[j - 1] == '.':
                e1 = True
            if j < n - 1 and s[j + 1] == '.':
                e2 = True
            if e1 and e2:
                cc += 2 if c == '.' else -2
            elif e1 or e2:
                cc += 1 if c == '.' else -1
            s[j] = c
            res[i] = cc
    for r in res:
        print(r)


f()
