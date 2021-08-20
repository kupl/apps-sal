MOD = 10 ** 9 + 7


def pow_mod(x, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return pow_mod(x ** 2 % MOD, n // 2) % MOD
    else:
        return x * pow_mod(x ** 2 % MOD, n // 2) % MOD


(N, K) = map(int, input().split())
ans = 0
rec = [0] * (K + 1)
for X in range(K, 0, -1):
    rec[X] = pow_mod(K // X, N)
    for i in range(2, K // X + 1):
        rec[X] = (rec[X] - rec[i * X]) % MOD
    ans = (ans + X * rec[X]) % MOD
print(ans)
