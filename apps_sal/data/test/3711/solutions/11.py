def main():
    a, b, c = list(map(int, input().split()))
    res, c = [-1], c + 1
    if c < a + b:
        for n, m, k in (a, b, c), (b, a, c):
            if n < k:
                k -= n - 1
                n, m = m, 1
            res.append(n // k * m)
    print(max(res))


def __starting_point():
    main()

__starting_point()
