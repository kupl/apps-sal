
import time

x = []
y = []

for i in range(3):
    (a, b) = (int(i) for i in input().split())
    x.append(a)
    y.append(b)

if len(set(x)) == 2:
    (x, y) = (y, x)

a = [[x[i], y[i]] for i in range(3)]
a = sorted(a)

start = time.time()

if (a[0][0] == a[1][0] and a[1][0] == a[2][0]) or (a[0][1] == a[1][1] and a[1][1] == a[2][1]):
    print(1)
elif a[0][0] == a[1][0] or a[1][0] == a[2][0] or a[0][1] == a[1][1] or a[1][1] == a[2][1]:
    print(2)
else:
    print(3)

finish = time.time()
