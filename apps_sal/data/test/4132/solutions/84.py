from math import gcd

n = int(input())
a = list(map(int, input().split()))


for i in range(n - 1):
    a[i + 1] = gcd(a[i], a[i + 1])

print(a[n - 1])
