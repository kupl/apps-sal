import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = list(map(int, input().split()))
P = [-1 for i in range(N)]
def par(a):
    L = []
    while P[a] >= 0:
        L.append(a)
        a = P[a]
    for l in L:
        P[l] = a
    return a
def unite(a, b):
    if par(a) == par(b): return 0
    if P[par(b)] == P[par(a)]:
        P[par(b)] = par(a)
        P[par(a)] -= 1
    elif P[par(b)] > P[par(a)]:
        P[par(b)] = par(a)
    else:
        P[par(a)] = par(b)

for _ in range(M):
    u, v = list(map(int, input().split()))
    unite(u-1, v-1)

C = [[] for _ in range(N)]
D = [0] * N
for i in range(N):
    C[par(i)].append(i)
    D[par(i)] = 1
ma = -1
ans = 0
for i in range(N):
    p = par(i)
    if D[p] == 0:
        continue
    D[p] = 0
    if min(C[p]) < ma:
        ans += 1
    ma = max(ma, max(C[p]))
print(ans)

