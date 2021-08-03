from bisect import bisect_left
n, m = map(int, input().split())
py = []
l = [[] for _ in range(n + 1)]
for _ in range(m):
    p, y = map(int, input().split())
    l[p].append(y)
    py.append((p, y))

for i in l:
    i.sort()

for p, y in py:
    s = str(p)
    t = str(bisect_left(l[p], y) + 1)
    ans = "0" * (6 - len(s)) + s + "0" * (6 - len(t)) + t
    print(ans)
