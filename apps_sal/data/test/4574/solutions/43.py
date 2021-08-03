N = int(input())
a = list(map(int, input().split()))
c = {}
d = [0, 0]
ans = 0

for i in a:
    if i not in c:
        c[i] = 0
    c[i] += 1

for i, v in zip(c.keys(), c.values()):
    if v >= 4:
        d.append(i)
        d.append(i)
    elif v >= 2:
        d.append(i)

d.sort(reverse=True)

if len(d) <= 3:
    ans = max(ans, 0)
else:
    ans = max(ans, d[0] * d[1])

print(ans)
