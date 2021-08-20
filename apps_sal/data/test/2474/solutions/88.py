MOD = 10 ** 9 + 7
N = int(input())
C = list(sorted(map(int, input().split()), reverse=True))
ans = 0
pow_list = [1] * (N + 1)
for i in range(1, N + 1):
    pow_list[i] = 2 * pow_list[i - 1] % MOD
base = pow_list[N]
for (i, c) in enumerate(C):
    now = pow_list[N - i - 1]
    tot = 0
    if i >= 1:
        tot = pow_list[i] + i * pow_list[i - 1]
    else:
        tot = pow_list[i]
    ans += tot * now * c % MOD
    ans %= MOD
print(ans * base % MOD)
