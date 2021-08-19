n, m, k = [int(x) for x in input().split()]
r = [(0, -1) for i in range(n)]
c = [(0, -1)for i in range(m)]

for i in range(k):
    ax, crd, clr = [int(x) for x in input().split()]
    if ax == 1:
        r[crd - 1] = (clr, i)
    else:
        c[crd - 1] = (clr, i)  # ax === 2
for i in range(n):
    s = []
    for j in range(m):
        clr = r[i][0] if r[i][1] > c[j][1] else c[j][0]
        s.append(str(clr))
    print(" ".join(s))
