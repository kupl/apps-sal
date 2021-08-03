import random
n = int(input())
a = [int(x) for x in input().split()]
j = 1
b = [0] * (n + 1)
for i in a:
    b[i] = 1
c = []
for i, j in enumerate(b):
    if j == 0:
        c.append(i)
c = set(c)
for i in range(1, n + 1):
    i = i - 1
    if a[i] == 0:
        if i + 1 in c:
            for k in c:
                if k != i + 1:
                    a[i] = k
                    c.remove(k)
                    break
for i in range(1, n + 1):
    i = i - 1
    if a[i] == 0:
        for k in c:
            if k != i + 1:
                a[i] = k
                c.remove(k)
                break
for i in a:
    print(i, end=" ")
