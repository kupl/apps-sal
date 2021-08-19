n = int(input())
l = []
r = []
for i in range(0, n):
    (x, y) = map(int, input().split())
    l.append(x)
    r.append(y)
l.sort()
r.sort()
res = n
for i in range(0, n):
    res += max(l[i], r[i])
print(res)
