import sys
stdin = sys.stdin
sys.setrecursionlimit(10**6)
ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
nn = lambda: list(stdin.readline().split())
ns = lambda: stdin.readline().rstrip()

n = ni()
g = [[] for i in range(n)]

for i in range(n-1):
    a,b = na()
    g[a-1].append((b-1,i))

ans = [-1]*(n-1)
m = [0]*n

for i in range(n):
    k = 1
    for c,j in g[i]:
        if m[i] == k: k += 1
        m[c] = k
        ans[j] = k
        k+=1

print(max(m))
print('\n'.join([str(u) for u in ans]))
