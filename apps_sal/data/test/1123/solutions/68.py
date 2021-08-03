import math
from collections import defaultdict

N, K = list(map(int, input().split()))
mod = 10**9 + 7
DP = [0] * (K + 1)  # DP[i]:gcd=iとなる数列の個数
ans = 0

for i in range(K, 0, -1):
    m = K // i  # m:iの倍数の個数
    DP[i] = pow(m, N, mod)
    for j in range(2, m + 1):
        DP[i] -= DP[i * j]
    ans += (DP[i] * i) % mod
    ans %= mod

print(ans)
