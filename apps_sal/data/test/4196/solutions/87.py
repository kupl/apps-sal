from math import gcd
n = int(input())
a = list(map(int, input().split()))
l, r = [a[0]] * n, [a[n - 1]] * n
for i in range(1, n - 1):
    l[i] = gcd(l[i - 1], a[i])
    r[n - i - 1] = gcd(r[n - i], a[n - i - 1])
ans = [0] * n
ans[0] = r[1]
ans[n - 1] = l[n - 2]
for i in range(1, n - 1):
    ans[i] = gcd(l[i - 1], r[i + 1])
print(max(ans))
