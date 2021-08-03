import sys

readline = sys.stdin.readline


def ns(): return readline().rstrip()
def ni(): return int(readline().rstrip())
def nm(): return map(int, readline().split())
def nl(): return list(map(int, readline().split()))


n = ni()
G = [list() for _ in range(n)]
for _ in range(n - 1):
    a, b = nm()
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)


mod = 10**9 + 7
dub = [1] * (n + 1)
for i in range(n):
    dub[i + 1] = dub[i] * 2
    if dub[i + 1] > mod:
        dub[i + 1] -= mod

size = [-1] * n
q = [0]
while q:
    v = q[-1]
    if size[v] < 0:
        for x in G[v]:
            if size[x] < 0:
                q.append(x)
        size[v] = 0
    else:
        size[v] = 1
        for x in G[v]:
            size[v] += size[x]
        q.pop()

ans = 0
for v in range(n):
    c = 0
    res = 1
    for x in G[v]:
        if size[x] < size[v]:
            c += size[x]
            res += dub[size[x]] - 1
    res += dub[n - 1 - c] - 1
    res %= mod
    ans = (ans + dub[n - 1] - res) % mod
print(ans * pow(dub[n], mod - 2, mod) % mod)
