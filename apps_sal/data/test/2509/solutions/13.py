import sys
readline = sys.stdin.readline


def main():
    (N, K) = map(int, readline().rstrip().split())
    if K == 0:
        print(N ** 2)
        return
    ans = 0
    for b in range(K, N + 1):
        r = (N + 1) % b
        p = (N + 1) // b
        ans += (b - K) * p + max(0, r - K)
    print(ans)


def __starting_point():
    main()


__starting_point()
