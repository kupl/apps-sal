from math import gcd
n = int(input())
a = [int(x) for x in input().split()]
boss = max(a)
arr = 0
g = 0
for i in range(n):
    a[i] = boss - a[i]
    g = gcd(g, a[i])
for item in a:
    arr += item // g
print(arr, g)
