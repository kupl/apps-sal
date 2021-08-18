
def resolve():
    MOD = 10 ** 9 + 7
    N = int(input())
    C = sorted(map(int, input().split()))
    P = [1] * (N + 1)
    for i in range(N):
        P[i + 1] *= P[i] * 2
        P[i + 1] %= MOD
    ans = 0
    for i in range(N):
        l, r = i, N - i - 1
        now = P[r]
        if r != 0:
            now += P[r - 1] * r
        now *= P[l]
        now *= C[i]
        ans += now
        ans %= MOD
    ans *= P[N]
    print(ans % MOD)


def __starting_point():
    resolve()


__starting_point()
