__author__ = 'asmn'
import sys



n, m = tuple(map(int, input().split()))
v = list(map(int, input().split()))
e = [[] for i in range(n)]
for k in range(m):
    x, y = tuple(map(int, input().split()))
    e[x - 1].append(y - 1)
    e[y - 1].append(x - 1)

nx = sorted(list(range(n)), key=lambda x: v[x], reverse=True)

used = set()
ans = 0
for x in nx:
    for y in e[x]:
        if y not in used:
            ans += v[y]
    used.add(x)
print(ans)


