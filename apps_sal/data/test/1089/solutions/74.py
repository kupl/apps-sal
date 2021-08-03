#!/usr/bin/env python3
def main():
    N, M, K = list(map(int, input().split()))
    m = 10**9 + 7
    # 方針: ２つの駒の距離だけ考えれば良い、それ以外K-2個の駒の位置が(N*M-2)C(K-2)通りある
    # マンハッタン距離はx方向とy方向を独立に扱える
    ans = 0
    for d in range(1, M):
        ans += (d * (M - d) % m) * pow(N, 2, m) % m
        ans %= m

    for d in range(1, N):
        ans += (d * (N - d) % m) * pow(M, 2, m) % m
        ans %= m

    # 答えに(NM-2)C(K-2)かける
    # K回しか処理しないから間に合う
    for r in range(K - 2):
        ans *= ((N * M % m - 2) % m - r) % m
        ans %= m
        ans *= pow(r + 1, m - 2, m)
        ans %= m
    print(ans)


def __starting_point():
    main()


__starting_point()
