import math
N, X = map(int, input().split())
x = list(map(int, input().split()))
x.append(X)
x.sort()
d = []
if N == 1:
    print(x[1] - x[0])
    return
for i in range(N):
    d.append(x[i + 1] - x[i])
gc = math.gcd(d[0], d[1])
for i in range(N):
    gc = math.gcd(d[i], gc)
print(gc)
