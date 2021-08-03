d = {}
data = input().split()
k = int(data[1])
data = input().split()
ans = 0
for el in data:
    v = int(el)
    p = [0, 0, ]

    if v in list(d.keys()):
        p = d[v]

    if v % k == 0 and (v / k) in list(d.keys()):
        ans += d[v / k][1]
        p[1] += d[v / k][0]

    p[0] += 1
    d[v] = p

print(ans)
