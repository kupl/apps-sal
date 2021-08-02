n, m = map(int, input().split())
f = [0] + list(map(int, input().split()))
z = [1] + [0] * (n + 1)
e = [[] for i in range(n + 1)]
for i in range(1, n):
    po, ki = map(int, input().split())
    e[po].append(ki)
    e[ki].append(po)
e[1] += [0]
r = [len(x) == 1 for x in e]
ans = 0
s = {(1, 0)}
while len(s):
    po, ki = s.pop()
    z[po] = 1
    if f[po]:
        ki += 1
    else:
        ki = 0
    if ki > m:
        continue
    if r[po]:
        ans += 1
    for x in e[po]:
        if z[x]:
            continue
        s |= {(x, ki)}
print(ans)
