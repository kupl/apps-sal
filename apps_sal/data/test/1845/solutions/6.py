n = int(input())
a = list(map(int, input().split()))
s = sum(a)
if n == 1:
    print(s)
    return
ans = s
c = {}
for i in range(n):
    if a[i] not in c:
        c[a[i]] = 0
    c[a[i]] += 1

ds = {}
for i in range(1, 102):
    ds[i] = []
    for j in range(1, i + 1):
        if i % j == 0:
            ds[i].append(j)

for v1 in c.keys():
    for v2 in c.keys():
        if v1 == v2 and c[v1] == 1:
            continue
        for d in ds[v1]:
            ch = -(v1 - v1 // d) + (v2 * d - v2)
            ans = min(ans, s + ch)

print(ans)
