from math import gcd
n = int(input())
a = list(map(int, input().split()))
res = a[0]
for i in range(1, len(a)):
    res = gcd(res, a[i])
print(res)
