def main():
    n, k, x = list(map(int, input().split()))
    aa = list(map(int, input().split()))
    x, lo, u = x ** k, [0] * n, 0
    for i, a in enumerate(aa):
        lo[i] = u
        u |= a
    hi, u = [], 0
    for a in reversed(aa):
        hi.append(u)
        u |= a
    hi.reverse()
    for i, u, a, v in zip(list(range(n)), lo, aa, hi):
        aa[i] = a * x | u | v
    print(max(aa))


def __starting_point():
    main()

__starting_point()
