def main():
    n, m = list(map(int, input().split()))
    wa = 0
    kaisuu = 1900 * (2 ** m)
    nokori = ((n - m) * 100) * (2 ** m)
    ikai = (1900 * m) + (100 * (n-m))
    print((ikai*(2**m)))

def __starting_point():
    main()

__starting_point()
