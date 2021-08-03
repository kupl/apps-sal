from math import gcd
n = int(input())
T = []
for i in range(n):
    T.append(int(input()))

tmp = T[0]
for i in range(1, n):
    g = gcd(tmp, T[i])
    tmp = T[i] * tmp // g

print(tmp)
