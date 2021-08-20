(n, k) = list(map(int, input().split()))
P = list(map(int, input().split()))
parent = list(range(256))
sz = [1] * 256


def rt(x):
    if x != parent[x]:
        parent[x] = rt(parent[x])
    return parent[x]


def u(rx, ry):
    parent[ry] = rx
    sz[rx] += sz[ry]


ans = [0] * n
for (i, p) in enumerate(P):
    rx = rt(p)
    while rx > 0 and sz[rx] + sz[rt(rx - 1)] <= k:
        u(rt(rx - 1), rx)
        rx = rt(p)
    ans[i] = rt(p)
print(' '.join(map(str, ans)))
