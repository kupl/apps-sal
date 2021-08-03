l = int(input())
# l = 1000000
r = 1
while 2 ** r <= l:
    r += 1
r = min(19, r - 1)
# print(r)

n = r + 1
# print(n)

ts = [i for i in range(1, n)]
ts.reverse()
# print(ts)

m = (n - 1) * 2

points = {}

for t in ts:
    a = l - 2 ** (t - 1)
    b = 2 ** r
    if a >= b:
        points[t] = a
        l -= 2 ** (t - 1)

m += len(points)
print((n, m))
for i in range(1, (n - 1) * 2 + 1):
    p = (i - 1) // 2 + 1
    if i % 2 == 0:
        print((p, p + 1, 0))
    else:
        print((p, p + 1, 2 ** (p - 1)))

for k in list(points.keys()):
    print((k, n, points[k]))
