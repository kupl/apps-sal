def main():
    M = 10**9 + 7
    N = 10**5 * 2
    fac = [0] * (N + 1)
    fac[0] = b = 1
    for i in range(1, N + 1):
        fac[i] = b = b * i % M
    inv = [0] * (N + 1)
    inv[N] = b = pow(fac[N], M - 2, M)
    for i in range(N, 0, -1):
        inv[i - 1] = b = b * i % M
    n, *t = open(0).read().split()
    n = int(n)
    e = [[]for _ in range(n)]
    for a, b in zip(*[map(int, t)] * 2):
        e[a - 1] += b - 1,
        e[b - 1] += a - 1,
    o = []
    s = [0]
    f = [1] * n
    while s:
        v = s.pop()
        f[v] = 0
        o += v,
        l = []
        for w in e[v]:
            if f[w]:
                l += w,
                s += w,
        e[v] = l
    sz1, sz2 = [0] * n, [0] * n
    dp1, dp2 = [0] * n, [0] * n
    c = [[]for _ in range(n)]
    for v in o[::-1]:
        s = b = 1
        c1, c2 = [1], [1]
        for w in e[v]:
            u = sz1[w]
            b = b * dp1[w] * inv[u] % M
            c1 += b,
            s += u
        b = 1
        for w in e[v][::-1]:
            b = b * dp1[w] * inv[sz1[w]] % M
            c2 += b,
        c[v] = c1, c2[-2::-1]
        sz1[v] = s
        dp1[v] = b * fac[s - 1] % M
    sz2[0] = 1
    dp2[0] = 1
    for v in o:
        l = len(e[v])
        c1, c2 = c[v]
        uv = sz2[v] - 1
        tv = dp2[v] * inv[uv]
        uv += sz1[v]
        for w, l, r in zip(e[v], c1, c2):
            tw = l * r % M
            uw = uv - sz1[w] - 1
            dp2[w] = tv * tw * fac[uw] % M
            sz2[w] = uw + 2
    a = []
    for dp1, dp2, sz1, sz2 in zip(dp1, dp2, sz1, sz2):
        sz1 -= 1
        sz2 -= 1
        a += str(dp1 * dp2 * inv[sz1] * inv[sz2] * fac[sz1 + sz2] % M),
    print('\n'.join(a))


main()
