from math import gcd


n, k = list(map(int, input().split()))
a, b = list(map(int, input().split()))

x = n * k
y = -1
for i in range(n):
    c = i * k + b - a
    if c < 0:
        c += n * k
    ans = n * k // gcd(n * k, c)
    x = min(x, ans)
    y = max(y, ans)

    c = i * k + (k - b) - a
    if c < 0:
        now += n * k
    ans = n * k // gcd(n * k, c)
    x = min(x, ans)
    y = max(y, ans)

print(x, y)
