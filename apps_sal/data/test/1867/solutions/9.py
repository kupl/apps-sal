mm = 0
mmi = []
f = [0] * (10 ** 6 + 5)
g = [[] for _ in range(10 ** 6 + 5)]
x = int(input())
l = list(map(int, input().split(' ')))
for i in range(x):
    f[l[i]] += 1
    g[l[i]].append(i + 1)
    if f[l[i]] > mm:
        mm = f[l[i]]
        mmi = [l[i]]
    elif f[l[i]] == mm:
        mmi.append(l[i])
a1 = 0
a2 = 0
minn = 1000000000
for i in mmi:
    if g[i][-1] - g[i][0] < minn:
        minn = g[i][-1] - g[i][0]
        a1 = g[i][0]
        a2 = g[i][-1]
print(a1, a2)
