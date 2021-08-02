d, gl = map(int, input().split())
p = []
g = []
for i in range(d):
    P, G = map(int, input().split())
    p.append(P)
    g.append(G)
ans = sum(p)
for i in range(1 << d):
    tmp = 0
    c = 0
    b = [0 for i in range(d)]
    for j in range(d):
        if i & (1 << j):
            tmp += g[j] + (j + 1) * p[j] * 100
            c += p[j]
            b[j] = 1
    s = d - 1
    while tmp < gl and s >= 0:
        if b[s] == 1:
            s -= 1
        else:
            for k in range(p[s]):
                tmp += 100 * (s + 1)
                c += 1
                if tmp >= gl:
                    break
            s -= 1
    ans = min(ans, c)
print(ans)
