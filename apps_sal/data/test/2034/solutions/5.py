n, m = map(int, input().split())
e = [[] for i in range(n + 1)]
f = [0] * (n + 1)
ans = 0
for i in range(m):
    po, ki = map(int, input().split())
    e[po].append(ki)
    e[ki].append(po)
for i in range(1, n + 1):
    if f[i]:
        continue
    ch = [(i, 0)]
    f[i] = 1
    fl = 1
    while ch != []:
        nom, pre = ch.pop(0)
        for x in e[nom]:
            if x == pre:
                continue
            if f[x] == 1:
                fl = 0
            if f[x] == 0:
                ch.append((x, nom))
                f[x] = 1
    ans += fl
print(ans)
