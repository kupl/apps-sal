n = int(input())
a = sorted([int(i) for i in input().split()])
m = int(input())
b = sorted([int(i) for i in input().split()])
ma = a1 = 3 * n
mb = b1 = 3 * m
rast = a1 - b1
(i, j) = (0, 0)
while i < n and j < m:
    z = min(a[i], b[j])
    while i < n and a[i] <= z:
        i += 1
        ma -= 1
    while j < m and b[j] <= z:
        j += 1
        mb -= 1
    if ma - mb > rast:
        (a1, b1) = (ma, mb)
        rast = a1 - b1
if 2 * n - 2 * m > rast:
    (a1, b1) = (2 * n, 2 * m)
print('%d:%d' % (a1, b1))
