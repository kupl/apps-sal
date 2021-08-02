import math

MOD = 10**9 + 7

ans = 0
N = int(input())
A = list(map(int, input().split()))

min_lcm = A[0]

# 最小公倍数を求める
for i in range(1, N):
    min_lcm = A[i] * min_lcm // math.gcd(A[i], min_lcm)


for i in range(N):
    ans += min_lcm // A[i]

print((ans % MOD))
