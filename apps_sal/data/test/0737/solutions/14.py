from math import sqrt
n = int(input())
a = int(sqrt(n))
if (a + 1) * (a + 1) <= n:
    a += 1
left = n - a * a
b = a
c = a + left // a
ans = 2 * b + 2 * c
if b * c < n:
    ans += 2
print(ans)

