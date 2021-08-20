N = int(input())
A = list(map(int, input().split()))
MOD = 10 ** 9 + 7
S = sum(A) % MOD
ans = 0
for i in range(N - 1):
    S -= A[i]
    S %= MOD
    ans += A[i] % MOD * S
    ans %= MOD
print(ans)
