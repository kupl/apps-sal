import math
(N, M, K) = list(map(int, input().split()))
MOD = 998244353


def getInvs(n, MOD):
    invs = [1] * (n + 1)
    for x in range(2, n + 1):
        invs[x] = -(MOD // x) * invs[MOD % x] % MOD
    return invs


invs = getInvs(N + 3, MOD)
num = M
nums = []
for i in reversed(list(range(1, N))):
    nums.append(num)
    num *= i * (M - 1)
    num *= invs[N - i]
    num %= MOD
nums.append(num)
nums.reverse()
ans = sum(nums[:K + 1])
ans %= MOD
print(ans)
