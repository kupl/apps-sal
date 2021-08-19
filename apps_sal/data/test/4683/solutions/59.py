MOD = 10 ** 9 + 7
N = int(input())
A = list(map(int, input().split()))
S = sum(A) % MOD
ans = 0
for x in A:
    S -= x
    S %= MOD
    ans += S * x
    ans %= MOD
ans %= MOD
print(ans)
