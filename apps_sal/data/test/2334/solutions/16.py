import math
n = int(input())
a = [int(s) for s in input().split()]
x, f = map(int, input().split())
ans = 0
for i in range(n):
    if a[i] <= x:
        continue
    if a[i] // (x + f) > 0:
        ans += (a[i] // (x + f)) * f
        a[i] -= a[i] // (x + f) * (x + f)
        if a[i] <= x:
            continue
        ans += a[i] // x * f
    else:
        ans += a[i] // x * f
print(ans)
