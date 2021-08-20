import sys
readline = sys.stdin.readline


def main():
    (N, M) = map(int, readline().rstrip().split())
    cakes = [tuple(map(int, readline().rstrip().split())) for _ in range(N)]
    res = -10 ** 15
    for a in [1, -1]:
        for b in [1, -1]:
            for c in [1, -1]:
                gains = [a * x + b * y + c * z for (x, y, z) in cakes]
                gains.sort(reverse=True)
                res = max(res, sum(gains[:M]))
    print(res)


def __starting_point():
    main()


__starting_point()
