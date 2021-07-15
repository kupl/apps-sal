import math
mod = 998244353
n = int(input())
p = [list(map(int, input().split())) for i in range(n)]
pow2 = [1]
for i in range(n):
    pow2.append(pow2[-1] * 2 % mod)
used = [[False] * n for i in range(n)]
ret = (pow2[n] - 1 - n - n * (n - 1) / 2) % mod
for i in range(n):
    for j in range(i):
        if used[i][j]:
            continue
        inline = [i, j]
        for k in range(n):
            if k == i or k == j:
                continue
            if (p[i][1] - p[k][1]) * (p[j][0] - p[k][0]) == (p[j][1] - p[k][1]) * (p[i][0] - p[k][0]):
                inline.append(k)
        for k in range(len(inline)):
            for l in range(len(inline)):
                used[inline[k]][inline[l]] = True
        v = len(inline)
        ret = (ret + mod - pow2[v] + 1 + v + v * (v - 1) // 2) % mod
print((int(ret)))

