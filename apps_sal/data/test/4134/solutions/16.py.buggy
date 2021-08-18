from collections import defaultdict
import itertools
n, m, k = list(map(int, input().split()))
A = [list(map(int, input().split())) for _ in range(n)]

if n == 1 and m == 1:
    if A[0][0] == k:
        print(1)
    else:
        print(0)
    return

ans = 0
s = (n - 1 + m - 1) // 2
t = (n - 1 + m - 1) - s
#print(s, t)
DS = [defaultdict(lambda:0) for key in range(n)]
for i in range(2**s):
    L = [0] * s
    for j in range(s):
        if (i >> j) & 1:
            L[j] = 1
    key = sum(L)
    if key > n - 1:
        continue
    y = 0
    x = 0
    res = A[0][0]
    for l in L:
        if l == 1:
            y += 1
        else:
            x += 1
        if 0 <= y < n and 0 <= x < m:
            res ^= A[y][x]
        else:
            break
    else:
        DS[key][res] += 1
# print(DS)
ans = 0
for i in range(2**t):
    L = [0] * t
    for j in range(t):
        if (i >> j) & 1:
            L[j] = 1
    tkey = sum(L)
    if tkey > n - 1:
        continue
    y = n - 1
    x = m - 1
    res = A[n - 1][m - 1]
    for idx, l in enumerate(L):
        if idx == len(L) - 1:
            continue
        if l == 1:
            y -= 1
        else:
            x -= 1
        if 0 <= y < n and 0 <= x < m:
            res ^= A[y][x]
        else:
            break
    else:
        skey = n - 1 - tkey
        sres = res ^ k
        #print(skey, sres)
        ans += DS[skey][sres]
print(ans)
