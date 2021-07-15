MOD = 998244353


def main():
    N, K = list(map(int, input().split()))
    ranges = [None] * K
    for i in range(K):
        L, R = list(map(int, input().split()))
        ranges[i] = (L, R)
    delta = [0] * (N+1)
    ans = [0] * (N+1)
    delta[1] = 1
    delta[2] = (-1) % MOD
    for i in range(1, N+1):
        ans[i] = (ans[i-1] + delta[i]) % MOD
        for L, R in ranges:
            if i + L <= N:
                delta[i+L] = (delta[i+L] + ans[i]) % MOD
            if i + R + 1 <= N:
                delta[i+R+1] = (delta[i+R+1] - ans[i]) % MOD
    print((ans[N]))


def __starting_point():
    main()

__starting_point()
