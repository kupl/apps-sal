import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ks = list(list(map(int, input().split())) for _ in range(m))
p = list(map(int, input().split()))

ans = 0

for i in range(2 ** n):
    c = [False] * n
    for j in range(n):
        if (i >> j) & 1: c[j] = True
    for j in range(m):
        count, l = 0, ks[j][0]
        for k in range(l):
            if c[ks[j][k + 1] - 1]: count += 1
        if count % 2 != p[j]: break
    else: ans += 1

print(ans)
