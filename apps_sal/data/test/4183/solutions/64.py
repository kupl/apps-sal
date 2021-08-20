from math import gcd
n = int(input())
T = [int(input()) for _ in range(n)]
ans = 1
for i in range(n):
    ans = ans * T[i] // gcd(ans, T[i])
print(ans)
