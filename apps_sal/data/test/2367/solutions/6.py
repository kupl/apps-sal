import sys
sys.setrecursionlimit(10000000)
MOD = 10 ** 9 + 7
INF = 10 ** 15


def main():
    (H, W, A, B) = map(int, input().split())
    MAXN = H + W + 3
    factorial = [1]
    for i in range(1, MAXN + 1):
        factorial.append(factorial[-1] * i % MOD)
    inv_factorial = [-1] * (MAXN + 1)
    inv_factorial[-1] = pow(factorial[-1], MOD - 2, MOD)
    for i in range(MAXN - 1, -1, -1):
        inv_factorial[i] = inv_factorial[i + 1] * (i + 1) % MOD

    def fact(N):
        return factorial[N]

    def nck(N, K):
        return 0 if K > N or K < 0 else factorial[N] * inv_factorial[N - K] * inv_factorial[K] % MOD

    def dist(sy, sx, gy, gx):
        return nck(gy - sy + gx - sx, gy - sy)
    ans = 0
    if H - A < W - B:
        (H, W) = (W, H)
        (A, B) = (B, A)
    for i in range(W - B):
        x = B + i + 1
        y = H - A - i
        ans += dist(1, 1, y, x) * dist(y, x, H, W) % MOD
        ans %= MOD
    print(ans)


def __starting_point():
    main()


__starting_point()
