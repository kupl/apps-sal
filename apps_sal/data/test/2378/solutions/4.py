import sys
sys.setrecursionlimit(10 ** 6)
readline = sys.stdin.readline
n = int(input())
g = [[] for _ in range(n)]
for i in range(n - 1):
    (a, b) = [int(i) for i in readline().split()]
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)
cnt = [-1] * n
parent = [-1] * n
q = [0]
order = []
while q:
    v = q.pop()
    order.append(v)
    for c in g[v]:
        if parent[v] != c:
            parent[c] = v
            q.append(c)
MOD = 10 ** 9 + 7
pow2 = [1]
for i in range(n):
    pow2.append(pow2[-1] * 2 % MOD)
num = [0] * n
ans = 0
for v in reversed(order):
    res = 1
    nokori = n - 1
    for c in g[v]:
        if c != parent[v]:
            nc = num[c] + 1
            res += pow2[nc] - 1
            num[v] += nc
            nokori -= nc
    res += pow2[nokori] - 1
    ans += pow2[n - 1] - res
R = (MOD + 1) // 2
print(ans * pow(R, n, MOD) % MOD)
