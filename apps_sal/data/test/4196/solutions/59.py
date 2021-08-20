import sys


def gcd(m, n):
    if n == 0:
        (n, m) = (m, n)
    r = m % n
    return gcd(n, r) if r else n


n = int(input())
a = list(map(int, sys.stdin.readline().split()))
(l, r) = ([0] * (n + 1), [0] * (n + 1))
for i in range(1, n + 1):
    l[i] = gcd(l[i - 1], a[i - 1])
    r[n - i] = gcd(r[n - i + 1], a[n - i])
ans = 0
for i in range(n):
    m = gcd(l[i], r[i + 1])
    if ans < m:
        ans = m
print(ans)
