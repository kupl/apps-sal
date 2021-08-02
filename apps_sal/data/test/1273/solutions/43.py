import sys
stdin = sys.stdin
sys.setrecursionlimit(10**6)
def ni(): return int(ns())
def na(): return list(map(int, stdin.readline().split()))
def nn(): return list(stdin.readline().split())
def ns(): return stdin.readline().rstrip()


n = ni()
g = [[] for i in range(n)]

for i in range(n - 1):
    a, b = na()
    g[a - 1].append((b - 1, i))

ans = [-1] * (n - 1)
m = [0] * n

for i in range(n):
    k = 1
    for c, j in g[i]:
        if m[i] == k:
            k += 1
        m[c] = k
        ans[j] = k
        k += 1

print(max(m))
print('\n'.join([str(u) for u in ans]))
