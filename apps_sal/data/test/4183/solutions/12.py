from math import *
N = int(input())
T = list((int(input()) for _ in range(N)))
ans = T[0]
for i in range(1, N):
    ans = ans * T[i] // gcd(ans, T[i])
print(ans)
