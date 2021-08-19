import sys
readline = sys.stdin.readline


def main():
    (N, K) = map(int, readline().rstrip().split())
    res = 0
    for b in range(1, N + 1):
        p = (N + 1) // b
        r = (N + 1) % b
        res += max(b - K, 0) * p + max(r - K, 0)
    if K == 0:
        print(N ** 2)
    else:
        print(res)


def __starting_point():
    main()


__starting_point()
