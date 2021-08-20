import math
n = int(input())
a = list(map(int, input().split()))
l = [0] * n
r = [0] * n
l[0] = a[0]
r[-1] = a[-1]
for i in range(n - 1):
    l[i + 1] = math.gcd(l[i], a[i + 1])
for i in reversed(range(n - 1)):
    r[i] = math.gcd(r[i + 1], a[i])
ans = max(l[-2], r[1])
for i in range(1, n - 1):
    ans = max(ans, math.gcd(l[i - 1], r[i + 1]))
print(ans)
