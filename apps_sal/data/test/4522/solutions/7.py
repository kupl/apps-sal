from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)

readline = sys.stdin.readline
N, M = map(int, readline().split())
E = []
for i in range(N-1):
    u, v, w = map(int, readline().split())
    E.append((w, u-1, v-1))
E.sort()
Q = set()
MP = defaultdict(list)
for i, q in enumerate(map(int, readline().split())):
    MP[q].append(i)
    Q.add(q)
Q = list(Q)
Q.sort()

def fact(N):
    return N*fact(N-1) % 100 if N > 1 else 1
fact(2000)

def root(x):
    if x == p[x]:
        return x
    y = x
    while y != p[y]:
        y = p[y]
    while x != y:
        p[x], x = y, p[x]
    return y
*p, = range(N)
sz = [1]*N
c = 0
def unite(x, y):
    nonlocal c
    px = root(x); py = root(y)
    if px == py:
        return 0
    c += sz[px] * sz[py]
    if sz[px] < sz[py]:
        p[py] = px
        sz[px] += sz[py]
    else:
        p[px] = py
        sz[py] += sz[px]
    return 1

k = 0
ans = [N*(N-1)//2]*M
L = len(Q)
for w, u, v in E:
    while k < L and Q[k] < w:
        e = Q[k]
        for i in MP[e]:
            ans[i] = c
        k += 1
    unite(u, v)
sys.stdout.write(" ".join(map(str, ans)))
sys.stdout.write("\n")
