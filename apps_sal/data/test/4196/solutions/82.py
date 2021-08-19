from math import gcd
n = int(input())
a = list(map(int, input().split()))
l = [0 for i in range(n)]
r = [0 for i in range(n)]
l[0] = a[0]
r[0] = a[-1]
for i in range(n - 1):
    l[i + 1] = gcd(l[i], a[i + 1])
for i in range(n - 1):
    r[i + 1] = gcd(r[i], a[-2 - i])
ans = [0 for i in range(n)]
for i in range(1, n - 1):
    ans[i] = gcd(l[i - 1], r[-i + n - 2])
ans[0] = r[n - 2]
ans[n - 1] = l[n - 2]
print(max(ans))
