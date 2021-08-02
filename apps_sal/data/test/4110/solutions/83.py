d, g = list(map(int, input().split()))
p = []
c = []
for i in range(d):
    P, C = list(map(int, input().split()))
    p.append(P)
    c.append(C)
ans = sum(p)
for i in range(2**d):
    z = i
    x = []
    for j in range(d):
        x.append(z % 2)
        z = z // 2
    po = 0
    m = 0
    for j in range(d):
        if x[j] == 1:
            po += 100 * (j + 1) * p[j] + c[j]
            m += p[j]
    q = [[] for j in range(d)]  # 残りp、c
    s = 0
    for j in range(d):
        if x[j] == 0:
            q[s].append(100 * (j + 1))
            q[s].append(p[j])
            s += 1
    q = [q[j] for j in range(d) if q[j] != []]
    q = sorted(q, reverse=True)
    w = len(q)
    for j in range(w):
        q[j][1] -= 1
    if po >= g:
        ans = min(ans, m)
    else:
        for j in range(w):
            if po + q[j][0] * q[j][1] >= g:
                m += (g - po + q[j][0] - 1) // q[j][0]
                ans = min(ans, m)
                break
            else:
                po += q[j][0] * q[j][1]
                m += q[j][1]
print(ans)
