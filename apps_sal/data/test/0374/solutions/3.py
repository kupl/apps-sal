n = int(input())
a = [int(x) for x in input().split()]
g = [0] * n
for i in range(n - 1):
    if type(g[a[i] - 1]) == int:
        g[a[i] - 1] = []
    g[a[i] - 1].append(i + 1)
a = [int(x) for x in input().split()]
b = [0] * n
now = [0] * n
for i in range(n - 1, -1, -1):
    if g[i] == 0:
        b[i] = 1
        now[i] = a[i]
        continue
    maxi = 0
    for x in g[i]:

        b[i] += b[x]
        if a[x] < 0:
            a[i] += a[x]
            a[x] = 0
        maxi = max(maxi, now[x])
    for x in g[i]:
        a[i] -= (maxi - now[x]) * b[x]
        now[x] = maxi
    now[i] = maxi
    if a[i] < 0:
        continue
    now[i] += (a[i] + b[i] - 1) // (b[i])
    a[i] -= (a[i] + b[i] - 1) // b[i] * b[i]

print(now[0])
