import sys
input = sys.stdin.readline
(n, m) = list(map(int, input().split()))
a = []


def f(x, y):
    res = 0
    if x[0] != y[0]:
        res += 1
    if x[1] != y[1]:
        res += 1
    if x[2] != y[2]:
        res += 1
    return res


if n >= 4 and m >= 4:
    for i in range(n):
        a.append(list(input()))
    print(-1)
elif n == 1 or m == 1:
    for i in range(n):
        a.append(list(input()))
    print(0)
elif n == 2 or m == 2:
    c = []
    if m == 2:
        for i in range(n):
            s = list(input())
            c.append(s.count('1') % 2)
    elif n == 2:
        for i in range(n):
            a.append(list(input()))
        for i in range(m):
            tmp = 0
            if a[0][i] == '1':
                tmp += 1
            if a[1][i] == '1':
                tmp += 1
            c.append(tmp % 2)
    res1 = 0
    res2 = 0
    for i in range(len(c)):
        if i % 2 == c[i]:
            res1 += 1
        else:
            res2 += 1
    print(min(res1, res2))
else:
    a = []
    if n == 3:
        b = list(input())
        c = list(input())
        d = list(input())
        for i in range(m):
            a.append(b[i] + c[i] + d[i])
    elif m == 3:
        s = input()
        a.append(s)
    r = max(n, m)
    res1 = 0
    res2 = 0
    res3 = 0
    res4 = 0
    for i in range(r):
        if i % 2 == 0:
            res1 += min(f(a[i], '111'), f(a[i], '000'))
            res2 += min(f(a[i], '010'), f(a[i], '101'))
            res3 += min(f(a[i], '110'), f(a[i], '001'))
            res4 += min(f(a[i], '011'), f(a[i], '100'))
        else:
            res2 += min(f(a[i], '111'), f(a[i], '000'))
            res1 += min(f(a[i], '010'), f(a[i], '101'))
            res4 += min(f(a[i], '110'), f(a[i], '001'))
            res3 += min(f(a[i], '011'), f(a[i], '100'))
    print(min(res1, res2, res3, res4))
