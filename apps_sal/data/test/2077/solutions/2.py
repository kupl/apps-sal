import sys
input = sys.stdin.buffer.readline
n, m = list(map(int, input().split()))
con = [[] for _ in range(n)]
for _ in range(m):
    a, b = list(map(int, input().split()))
    con[a - 1].append(b - 1)
    con[b - 1].append(a - 1)
t = [int(x) for x in input().split()]
od = sorted(list(range(n)), key=lambda f: t[f])
cn = [1] * n
ans = []
for ii in od:
    tt = t[ii]
    if cn[ii] != tt:
        print(-1)
        return
    for jj in con[ii]:
        if cn[jj] == tt:
            cn[jj] += 1
    ans.append(ii + 1)
print(" ".join(map(str, ans)))
