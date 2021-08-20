import sys
input = sys.stdin.readline
P = 10 ** 9 + 7


def main():
    (N, K) = list(map(int, input().split()))
    ans = 0
    n_gcd = [0] * (K + 1)
    for k in reversed(list(range(1, K + 1))):
        n = pow(K // k, N, mod=P)
        for m in range(2, K // k + 1):
            n -= n_gcd[k * m]
        n_gcd[k] = n % P
        ans = (ans + k * n_gcd[k]) % P
    print(ans)


def __starting_point():
    main()


__starting_point()
