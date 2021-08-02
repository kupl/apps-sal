import sys
import math
# input=sys.stdin.readline
# sys.setrecursionlimit(1000000)
I = lambda: list(map(int, input().split()))
ma = int(10000000000000000)
n, m = map(int, input().split())
a = [ma] * (515); a1 = [ma] * (515); fr = [0] * (515); pos = [0] * (515)
for i in range(n):
    b = I()
    x = int(0)
    for j in range(1, b[0] + 1):
        b[j] -= 1
        x |= (1 << b[j])
    fr[x] += 1

min1 = int(ma)
max1 = int(0)
ind, ind1 = int(), int()
for i in range(m):
    b = I()
    x = int(0)
    for j in range(2, b[1] + 2):
        b[j] -= 1
        x |= (1 << b[j])
    if a[x] != ma:
        if fr[x] > max1:
            max1 = fr[x]
            min1 = a[x] + b[0]
            ind = pos[x]
            ind1 = i + 1
        elif fr[x] == max1:
            if b[0] + a[x] < min1:
                min1 = b[0] + a[x]
                ind = pos[x]
                ind1 = i + 1
    if a[x] > b[0]:
        a[x] = b[0]
        pos[x] = i + 1


for i in range(1, 512):
    for j in range(1, 512):
        if i == j or a[i] == ma or a[j] == ma:
            continue
        k = i | j
        cnt = int(0)
        while k > 0:
            cnt += fr[k]
            k = (k - 1) & (i | j)
        if cnt > max1:
            ind = pos[i]
            ind1 = pos[j]
            max1 = cnt
            min1 = a[i] + a[j]
        if cnt == max1:
            if a[i] + a[j] < min1:
                ind = pos[i]
                ind1 = pos[j]
            min1 = min(min1, a[i] + a[j])

print(ind, ind1, sep=" ")
