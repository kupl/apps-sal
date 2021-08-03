from math import *
ans = 0
for _ in range(int(input())):
    si, di = list(map(int, input().split()))
    if si >= ans:
        ans = si + 1
        continue
    n = ans - si
    ans = si + ceil(n / di) * di + 1
print(ans - 1)
