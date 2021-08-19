n = int(input())
x = []
y = []
for i in range(n):
    (a, b) = map(int, input().split())
    x.append(a)
    y.append(b)
a = []
b = []
for i in range(n):
    (c, d) = map(int, input().split())
    a.append(c)
    b.append(d)
f = True
z = 0
while f:
    (tx, ty) = (x[0] + a[z], y[0] + b[z])
    s = set([(tx - a[i], ty - b[i]) for i in range(n)])
    if s == set(((x[i], y[i]) for i in range(n))):
        print(tx, ty)
        break
    z += 1
