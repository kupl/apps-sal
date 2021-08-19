def main():
    from collections import defaultdict
    import sys
    input = sys.stdin.readline
    (H, W, N) = map(int, input().split())
    g = defaultdict(int)
    for _ in range(N):
        (a, b) = (int(x) - 1 for x in input().split())
        for i in range(3):
            if a - i < 0:
                continue
            if a - i + 3 > H:
                continue
            for j in range(3):
                if b - j < 0:
                    continue
                if b - j + 3 > W:
                    continue
                g[(a - i) * W + (b - j)] += 1
    ctr = [0] * 10
    tot = (H - 2) * (W - 2)
    for cnt in g.values():
        ctr[cnt] += 1
        tot -= 1
    ctr[0] = tot
    print(*ctr, sep='\n')


def __starting_point():
    main()


__starting_point()
