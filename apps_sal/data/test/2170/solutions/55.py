# 写経
# https://atcoder.jp/contests/abc172/submissions/14794920

MOD = 10**9 + 7


def resolve():
    N, M = map(int, input().split())
    a = 1
    d = [1]
    for i in range(N):
        d.append(((M - N + i) * d[i] + i * d[i - 1]) % MOD)
        a = a * (M - i) % MOD
    print(a * d[-1] % MOD)


resolve()
