import math
(n, s) = tuple(map(int, input().split()))
x = []
y = []
k = []
r = []
for i in range(n):
    (a, b, c) = tuple(map(int, input().split()))
    x.append(a)
    y.append(b)
    k.append(c)
    r.append((math.sqrt(x[i] ** 2 + y[i] ** 2), i))
r.sort()
nas = s
i = 0
while i < n and nas < 1000000:
    nas += k[r[i][1]]
    i += 1
if i == n and nas < 1000000:
    print('-1')
else:
    print(r[i - 1][0])
