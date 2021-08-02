x, y, l, r = list(map(int, input().split()))

xx = []
yy = []
p = 1
xx.append(l - 1);
while p <= r:
    q = 1
    while p + q <= r:
        if p + q >= l and p + q <= r:
            xx.append(p + q)
        q *= y
    p *= x
xx.append(r + 1)
xx.sort()

for i in range(0, len(xx) - 1):
    yy.append(xx[i + 1] - xx[i] - 1)

print(max(yy))
