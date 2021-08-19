from math import gcd
(N, X) = list(map(int, input().split()))
x = list(map(int, input().split()))
dis = []
for i in range(N):
    dis.append(abs(X - x[i]))
res = 0
for i in range(N):
    res = gcd(res, dis[i])
print(res)
