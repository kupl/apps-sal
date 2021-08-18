import sys


n = int(input())

a = 1
cmod = 10 ** 9 + 7
for i in range(3 * n):
    a *= 3
    a %= cmod

b = 1
for i in range(n):
    b *= 7
    b %= cmod

ans = (a - b + cmod) % cmod
print(ans)
