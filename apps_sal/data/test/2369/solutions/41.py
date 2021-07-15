def ext_euc(a, b):
    if b == 0:
        return 1, 0, a
    y, x, v = ext_euc(b, a % b)
    y -= (a // b) * x
    return x, y, v


def mod_inv(a, mod):
    x, _, _ = ext_euc(a, mod)
    return x % mod


def main():
    MOD = 10 ** 9 + 7
    N, K = list(map(int, input().split(' ')))
    A = list(map(int, input().split(' ')))
    A.sort()
    comb = [0 for _ in range(N)]  # comb[i] = i_C_(K-1)
    v = 1
    for i in range(K - 1, N):
        comb[i] = v
        v *= i + 1
        v *= mod_inv(i - K + 2, MOD)
        v %= MOD
    ans = 0
    for i, a in enumerate(A):
        ans += a * (comb[i] - comb[N - i - 1])
        ans %= MOD
    print(ans)


def __starting_point():
    main()
__starting_point()
