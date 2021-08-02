from collections import deque
import sys
def input(): return sys.stdin.readline().rstrip()


mod = 10**9 + 7
n = int(input())
edge = [[] for i in range(n)]
for i in range(n - 1):
    a, b = list(map(int, input().split()))
    edge[a - 1].append(b - 1)
    edge[b - 1].append(a - 1)
inf = 10**6
Par = [inf] * n
Par[0] = -1
Deg = [0] * n
Deg[0] = 0
Chk = [0]
while Chk:
    c = Chk.pop()
    for next in edge[c]:
        if Par[next] == inf:
            Par[next] = c
            Deg[next] += 1
            Chk.append(next)

TS = list(v for v in range(n) if Deg[v] == 0)
D = deque(TS)
while D:
    v = D.popleft()
    for t in edge[v]:
        if t != Par[v]:
            Deg[t] -= 1
            if Deg[t] == 0:
                D.append(t)
                TS.append(t)

Used = [False] * n
C = [0] * n
for i in reversed(list(range(n))):
    v = TS[i]
    Used[v] = True
    for g in edge[v]:
        if not Used[g]:
            C[g] += C[v] + 1

H = [0] * n
H[0] = 1
H[1] = pow(2, mod - 2, mod)
for i in range(2, n):
    H[i] = (H[i - 1] * H[1]) % mod

ans = 0
for i in range(n):
    if len(edge[i]) == 1:
        continue
    else:
        A = []
        for e in edge[i]:
            if e == Par[i]:
                A.append(n - 1 - C[i])
            else:
                A.append(C[e] + 1)
        cur = 1 + (len(edge[i]) - 1) * H[-1]
        for a in A:
            cur -= H[n - 1 - a]
        ans = (ans + cur) % mod
print(((ans * H[1]) % mod))
