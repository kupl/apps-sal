import math


def lcm(x, y):
    return x * y // math.gcd(x, y)


(n, m) = map(int, input().split())
l = list(map(int, input().split()))
a = l[0] // 2
for i in range(n - 1):
    a = lcm(a, l[i + 1] // 2)
ok = True
for i in range(n):
    if a // (l[i] // 2) % 2 != 1:
        ok = False
        break
ans = 0
if ok:
    ans = (m // a + 1) // 2
print(ans)
