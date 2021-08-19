(p, q, r) = map(int, input().split())


def comb_mod(N, K, modp):
    K_fact = 1
    NK_fact = 1
    N_fact = 1
    for i in range(1, K + 1):
        K_fact *= i
        K_fact = K_fact % modp
    for i in range(1, N - K + 1):
        NK_fact *= i
        NK_fact = NK_fact % modp
    for i in range(1, N + 1):
        N_fact *= i
        N_fact = N_fact % modp
    K_inv = pow(K_fact, -1, modp)
    NK_inv = pow(NK_fact, -1, modp)
    pat = N_fact * K_inv % modp * NK_inv % modp
    return pat


pat = comb_mod(p * q - 2, r - 2, 10 ** 9 + 7)
ans = 0
for i in range(0, q + 1):
    ans += i * (q - i) * p * p
    ans = ans % (10 ** 9 + 7)
for k in range(0, p + 1):
    ans += k * (p - k) * q * q % (10 ** 9 + 7)
    ans = ans % (10 ** 9 + 7)
print(ans * pat % (10 ** 9 + 7))
