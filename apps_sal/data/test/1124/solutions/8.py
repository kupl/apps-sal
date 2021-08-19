# ARC105 B

from math import gcd


N = int(input())
A = list(map(int, input().split()))

ans = 0
for i in range(N):
    ans = gcd(ans, A[i])

print(ans)
