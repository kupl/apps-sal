n = int(input())
nv = (n + 2) * [0]
v = [int(i) for i in input().split()]
f = (n + 2) * [0]
go = list(map(int, list(range(1, n + 2))))
m = int(input())
p = []
for i in range(m):
    c = [int(i) for i in input().split()]
    if c[0] == 1:
        k = c[1] - 1
        vv = c[2]
        kk = k
        r = 0
        while vv > 0 and kk < n:
            if vv <= v[kk] - nv[kk]:
                nv[kk] = nv[kk] + vv
                vv = 0
                break
            else:
                vv = vv - (v[kk] - nv[kk])
                nv[kk] = v[kk]
                f[r] = kk
                r = r + 1
                kk = go[kk]
        for j in range(r):
            go[f[j]] = kk
    if c[0] == 2:
        p.append(nv[c[1] - 1])
for i in p:
    print(i)
