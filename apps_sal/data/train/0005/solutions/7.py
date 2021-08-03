from math import *

mod = 1000000007

for zz in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    ans = []
    cs = set()
    d = {}
    c = 0
    for i in range(n):
        if a[i] not in d:
            c += 1
            d[a[i]] = 0
        d[a[i]] += 1
    mv = 0
    m = [0] * n
    m[-1] = a[-1]
    for i in range(n - 2, -1, -1):
        m[i] = max(m[i + 1], a[i])

    for i in range(n):
        mv = max(a[i], mv)
        if a[i] in cs:
            break
        cs.add(a[i])
        d[a[i]] -= 1
        if d[a[i]] <= 0:
            c -= 1
        if mv == i + 1 and c == n - i - 1 and m[i + 1] == n - i - 1:
            ans.append(i)
    print(len(ans))
    for i in ans:
        print(i + 1, n - i - 1)
