from math import factorial
x, y = map(int, input().split())
if (x + y) % 3 != 0:
    print(0)
    return
x, y = x - (x + y) // 3, y - (x + y) // 3
a, b = 1, 1
if min(x, y) < 0:
    print(0)
    return
if x > y:
    x, y = y, x
mod = 10**9 + 7
for i in range(x):
    a *= x + y - i
    b *= i + 1
    a, b = a % mod, b % mod
print(a * pow(b, mod - 2, mod) % mod)
