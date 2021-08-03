import sys
a, b, c = map(int, input().split())
n = 998244353
print(a * (a + 1) // 2 % n * b * (b + 1) // 2 % n * c * (c + 1) // 2 % n)
