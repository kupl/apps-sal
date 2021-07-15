from math import gcd

t = int(input())

for _ in range(t):
    r, b, k = list(map(int, input().split()))
    r, b = sorted([r, b])
    a = gcd(r, b)
    x = (b - a - 1) // r + 1
    print("REBEL" if x >= k else "OBEY")

