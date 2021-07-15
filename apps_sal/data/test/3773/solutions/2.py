def main():
    n = int(input())
    res = 0
    for (a, k) in [map(int, input().split()) for _ in range(n)]:
        while a >= k:
            m = a // k
            if a % k == 0:
                res ^= m
                break
            x = (a - k * m - 1) // (m + 1)
            a -= max(1, x) * (m + 1)
    print('Takahashi' if res != 0 else 'Aoki')


def __starting_point():
    main()
__starting_point()
