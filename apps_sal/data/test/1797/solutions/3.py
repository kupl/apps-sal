n = int(input())
data = list(map(int, input().split()))
gp = {i: i for i in range(n)}
sets = {i: [i] for i in range(n)}
for i in range(n):
    (u, v) = (i, data[i] - 1)
    if gp[u] != gp[v]:
        temp = gp[v]
        for i in sets[gp[v]]:
            gp[i] = gp[u]
            sets[gp[u]].append(i)
        del sets[temp]
l = []
for i in sets:
    l.append(len(sets[i]))
l.sort(reverse=True)
n = len(l)
if n == 1:
    print(l[0] * l[0])
else:
    ans = (l[0] + l[1]) ** 2
    for i in range(2, n):
        ans += l[i] ** 2
    print(ans)
