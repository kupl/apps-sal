import math
N, X = map(int, input().split())
x = list(map(int, input().split()))
ls = []
for i in range(N):
    ls.append(abs(x[i] - X))
now = ls[0]
for i in range(1, N):
    now = math.gcd(ls[i], now)
print(now)
