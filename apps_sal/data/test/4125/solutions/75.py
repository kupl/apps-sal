import math

n, x = map(int, input().split())
xi = list(map(int, input().split()))

xi = list(map(lambda z: abs(z - x), xi))
g = xi[0]
for i in range(1, n):
    g = math.gcd(g, xi[i])
print(g)
