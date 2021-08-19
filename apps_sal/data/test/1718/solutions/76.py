import math


def lmi():
    return list(map(int, input().split()))


def main():
    (N, K) = lmi()
    A = lmi()
    one_idx = A.index(1)
    L = one_idx
    R = N - one_idx - 1
    ans = L // (K - 1) + R // (K - 1)
    ans += math.ceil((L % (K - 1) + R % (K - 1)) / (K - 1))
    print(ans)


def __starting_point():
    main()


__starting_point()
