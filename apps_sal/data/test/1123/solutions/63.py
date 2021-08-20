MOD = 10 ** 9 + 7
(N, K) = list(map(int, input().split()))
nums = [0] * (K + 1)
for i in reversed(list(range(1, K + 1))):
    num = pow(K // i, N, MOD)
    for j in range(2 * i, K + 1, i):
        num -= nums[j]
    nums[i] = num % MOD
ans = 0
for i in range(1, K + 1):
    ans += i * nums[i] % MOD
    ans %= MOD
print(ans)
