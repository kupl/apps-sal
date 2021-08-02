from math import gcd
a, b = map(int, input().split())
g, ans = gcd(a, b), 0
a, b = a // g, b // g
while a % 2 == 0:
    a //= 2
    ans += 1
while a % 3 == 0:
    a //= 3
    ans += 1
while a % 5 == 0:
    a //= 5
    ans += 1
while b % 2 == 0:
    b //= 2
    ans += 1
while b % 3 == 0:
    b //= 3
    ans += 1
while b % 5 == 0:
    b //= 5
    ans += 1
print(-1 if a != 1 or b != 1 else ans)
