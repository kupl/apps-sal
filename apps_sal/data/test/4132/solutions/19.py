import math
n = int(input())
a = list(map(int, input().split()))

g = math.gcd(a[0], a[1])
for i in range(2, n):
    g = math.gcd(g, a[i])

print(g)
