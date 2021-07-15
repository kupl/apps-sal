import sys

n = int(input())
a, b = [], []
for i in range(n):
    x, y = list(map(int, input().split()))
    a.append(x)
    b.append(y)
if sum(a) % 2 == sum(b) % 2 == 0:
    print(0)
else:
    for i in range(n):
        a[i], b[i] = b[i], a[i]
        if sum(a) % 2 == sum(b) % 2 == 0:
            print(1)
            return
        a[i], b[i] = b[i], a[i]
    for i in range(n):
        for j in range(i + 1, n):
            a[i], b[i] = b[i], a[i]
            a[j], b[j] = b[j], a[j]
            if sum(a) % 2 == sum(b) % 2 == 0:
                prin(2)
                return
            a[i], b[i] = b[i], a[i]
            a[j], b[j] = b[j], a[j]
    print('-1')

