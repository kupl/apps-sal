from math import gcd
n, x = map(int, input().split())
X = list(map(int, input().split()))
X.append(x)
X.sort()
g = X[1] - X[0]
for i in range(n):
    g = gcd(g, X[i + 1] - X[i])
print(g)
