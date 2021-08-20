from math import gcd
t = int(input())
a = list(map(int, input().split()))
n = a[0]
for c in a:
    n = gcd(n, c)
ans = 1
for i in range(2, int(n ** 0.5 + 0.5) + 1):
    if n % i == 0:
        kol = 0
        for x in range(100000000):
            if n % i == 0:
                kol += 1
                n //= i
            else:
                break
        ans *= kol + 1
if n > 1:
    ans *= 2
print(ans)
