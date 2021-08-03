import math
import itertools

n = int(input())
a = list(map(int, input().split()))
pf = [0] * (n + 1)
pb = [0] * (n + 1)
p = a[0]
for i in range(n):
    p = math.gcd(p, a[i])
    pf[i + 1] = p
p = a[-1]
for i in range(-1, -n - 1, -1):
    p = math.gcd(p, a[i])
    pb[i - 1] = p
ans = [0] * n
for i in range(n):
    ans[i] = math.gcd(pf[i], pb[i + 1])
print(max(ans))
