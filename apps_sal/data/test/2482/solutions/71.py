from collections import Counter
(n, k, l) = map(int, input().split())
city1 = [i for i in range(n)]
city2 = [i for i in range(n)]


def root(c, x):
    if x == c[x]:
        return x
    else:
        return root(c, c[x])


def union(c, x, y):
    rx = root(c, x)
    ry = root(c, y)
    if rx > ry:
        c[rx] = ry
    else:
        c[ry] = rx


for i in range(k):
    (a, b) = map(int, input().split())
    union(city1, a - 1, b - 1)
for i in range(l):
    (a, b) = map(int, input().split())
    union(city2, a - 1, b - 1)
r = []
for i in range(n):
    r.append((root(city1, i), root(city2, i)))
c = Counter(r)
for i in range(n):
    ans = c[r[i]]
    if i == n - 1:
        print(ans)
    else:
        print(ans, end=' ')
