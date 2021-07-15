
def main(stdin):
    n, d = next(stdin).split()
    n, d = int(n), int(d)
    a_i = sorted(map(int, next(stdin).split()))
    m = int(next(stdin))
    lost = 0

    a_sum = sum(int(a_i[i]) for i in range(min(m, n)))
    if n < m:
        lost = d * (m - n)
    print(a_sum - lost)


def __starting_point():
    import sys
    main(sys.stdin)

__starting_point()
