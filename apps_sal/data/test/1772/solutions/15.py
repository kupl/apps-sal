from math import *
n = int(input())
c = 0
nc = 0
k = input().split(" ")
for i in range(n):
    if (int(k[i]) % 2 == 0):
        c = c + 1
    else:
        nc = nc + 1
tt = min(c, nc) + max(0, nc - min(c, nc)) // 3
print(tt)
