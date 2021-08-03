from sys import setrecursionlimit as SRL, stdin

SRL(10 ** 7)
rd = stdin.readline
def rrd(): return map(int, rd().strip().split())


fa = [i for i in range(200005)]
s = [1] * 200005


def find(x):
    t = []
    while fa[x] != x:
        t.append(x)
        x = fa[x]
    for i in t:
        fa[i] = x
    return fa[x]


ans = [0] * 200005
n, q = rrd()

w = []
for i in range(n - 1):
    x, y, z = rrd()
    w.append([z, x, y])

w.sort(key=lambda x: x[0])
for x in w:
    u = find(x[1])
    v = find(x[2])

    ans[x[0]] += s[u] * s[v]
    fa[u] = v
    s[v] += s[u]

for i in range(1, 200001):
    ans[i] += ans[i - 1]

q = list(rrd())

for x in q:
    print(ans[x], end=' ')
