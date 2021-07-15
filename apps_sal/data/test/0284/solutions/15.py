from math import gcd

N = int(input())
x = 1234567
y = 123456
z = 1234

g = gcd(y, z)

if N % x == 0:
    print('YES')
    return

for a in range(N // x + 1):
    n = N - a * x

    if n % y == 0 or n % z == 0:
        print('YES')
        return
    if n % g != 0:
        continue

    x0 = -22 * n // 2
    y0 = 2201 * n // 2
    k = ((-x0) // (z // 2)) + 1
    x0 += k * z // 2
    y0 -= k * y // 2
    if y0 >= 0:
        print('YES')
        return

print('NO')

