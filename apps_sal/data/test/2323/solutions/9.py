from bisect import bisect_left


def main():
    n = int(input())
    s = sorted((int(si) for si in input().split()))
    ediff = sorted((x - s[i - 1] for (i, x) in enumerate(s) if i > 0))
    cumsum = [0] * n
    for i in range(n - 1):
        cumsum[i + 1] = cumsum[i] + ediff[i]
    q = int(input())
    for _ in range(q):
        (l, r) = list(map(int, input().split()))
        ind = bisect_left(ediff, r - l + 1)
        print((r - l + 1) * (n - ind) + cumsum[ind], end=' ')


def __starting_point():
    main()


__starting_point()
