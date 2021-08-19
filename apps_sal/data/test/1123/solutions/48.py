import sys
input = sys.stdin.readline
P = 10 ** 9 + 7


def main():
    (N, K) = list(map(int, input().split()))
    n_multiple = [0] * (K + 1)
    for k in range(1, K + 1):
        n_multiple[k] = K // k
    n_gcd = [0] * (K + 1)
    for k in reversed(list(range(1, K + 1))):
        n_gcd[k] = pow(n_multiple[k], N, mod=P)
        for m in range(2, K // k + 1):
            n_gcd[k] = (n_gcd[k] - n_gcd[k * m]) % P
    ans = 0
    for k in range(1, K + 1):
        ans = (ans + k * n_gcd[k]) % P
    print(ans)


def __starting_point():
    main()


__starting_point()
