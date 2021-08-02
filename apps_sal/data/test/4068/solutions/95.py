import sys

input = sys.stdin.readline

MOD = pow(10, 9) + 7


def MODINV(n: int, MOD=MOD):
    return pow(n, MOD - 2, MOD)


def main():
    N, M = list(map(int, input().split()))
    DP = [0] * (N + 1)
    ngset = set()
    for _ in range(M):
        a = int(input())
        ngset.add(a)

    DP[0] = 1
    if 1 not in ngset:
        DP[1] = DP[0]
    for i in range(2, N + 1):
        if i in ngset:
            continue
        DP[i] = DP[i - 1] + DP[i - 2]
        DP[i] %= MOD

    print((DP[N]))


def __starting_point():
    main()


__starting_point()
