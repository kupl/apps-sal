ax, ay, bx, by, tx, ty = list(map(int, input().split()))
n = int(input())
a, b = [], []
res = 0
for i in range(n):
    x, y = list(map(int, input().split()))
    lt = ((tx - x) * (tx - x) + (ty - y) * (ty - y))**0.5
    la = ((ax - x) * (ax - x) + (ay - y) * (ay - y))**0.5
    lb = ((bx - x) * (bx - x) + (by - y) * (by - y))**0.5
    a += [(la - lt, i)]
    b += [(lb - lt, i)]
    res += lt
a.sort()
b.sort()
res *= 2
if a[0][1] == b[0][1] and n > 1:
    res += min(a[0][0], b[0][0], a[0][0] + b[1][0], a[1][0] + b[0][0])
else:
    if a[0][1] == b[0][1]:
        res += min(a[0][0], b[0][0])
    else:
        res += min(a[0][0], b[0][0], a[0][0] + b[0][0])
print(res)
