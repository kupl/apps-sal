n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
c = list(map(int, input().split()))

ss = [(i, c[i]) for i in range(n)]
ss = sorted(ss, key=lambda x: (x[1], x[0]))
p = 0
ans1 = []
for _ in range(m):
    t, d = list(map(int, input().split()))
    t -= 1
    ans = 0
    c1 = min(d, a[t])
    a[t] -= c1
    ans += c1 * c[t]
    d -= c1
    while d > 0 and p < n:
        nt = ss[p][0]
        nc = ss[p][1]
        c2 = min(a[nt], d)
        a[nt] -= c2
        d -= c2
        ans += nc * c2
        if a[nt] == 0:
            p += 1
    if d == 0:
        print(ans)
    else:
        print(0)
