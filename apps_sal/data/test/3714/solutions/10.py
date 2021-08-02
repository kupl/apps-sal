from math import *
n = int(input())
a = list([int(s) - 1 for s in input().split()])
seen = [0] * n
ans = 1
lcm = 1
for i in range(n):
    if not seen[i]:
        j = i
        leng = 0
        while not seen[j]:
            seen[j] = 1
            leng += 1
            j = a[j]
        if i == j:
            if leng % 2 == 0:
                leng //= 2
            lcm = lcm // gcd(lcm, leng) * leng
        else:
            ans = -1
            break
if ans == -1:
    print(-1)
else:
    print(lcm)
