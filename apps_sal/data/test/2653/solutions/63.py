import sys
sys.setrecursionlimit(10**8)

n, q = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n-1)]
px = [list(map(int, input().split())) for _ in range(q)]

t = dict()
for i in range(1, n+1):
    t[i] = set()
for a, b in ab:
    t[a].add(b)
    t[b].add(a)

cnt = [0] * n
s = set()
for p, x in px:
    cnt[p-1] += x

def solve(p):
    s.add(p)
    for c in t[p]:
        if c not in s:
            cnt[c-1] += cnt[p-1]
            solve(c)
solve(1)
print(*cnt, sep=' ')

