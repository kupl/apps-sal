import math


def nop(a, b):
    l = 0
    for i in range(len(a)):
        d = a[i]
        while l < len(b) and b[l] != d:
            l += 1
        if l >= len(b) and b[l - 1] != d:
            return 0
        elif l < len(b) and b[l] != d:
            return 0
        l += 1
        if i < len(a) - 1 and l >= len(b):
            return 0
    return 1

a = int(input())
b = int(math.sqrt(a))
c = []
k = b
for i in range(k):
    if nop(str(b ** 2), str(a)) == 1:
        c.append(len(str(a)) - len(str(b ** 2)))
    b -= 1
c.sort()
if len(c) > 0:
    print(c[0])
else:
    print(-1)
