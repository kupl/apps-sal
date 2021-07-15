from collections import Counter

n = int(input())

c = list()

for i in range(n):
    c.append(int(input()))

c = Counter(c)

d = dict()

for k in c:
    v = c[k]
    if d.get(v, -1) != -1:
        d[v].append(k)
    else:
        d[v] = [k]

fl = False
for k in d:
    v = d[k]
    if len(v) > 1 and len(d) == 1 and len(v) == 2:
        fl = True
        print("YES")
        print(*v)
        break
if (not fl):
    print("NO")
