from itertools import combinations_with_replacement
import sys
read = sys.stdin.read
readlines = sys.stdin.readlines


def main():
    (n, m, q) = list(map(int, input().split()))
    qs = []
    for _ in range(q):
        abcd = tuple(map(int, input().split()))
        qs.append(abcd)
    A = tuple(combinations_with_replacement(list(range(1, m + 1)), n))
    r = 0
    for Ae in A:
        t0 = 0
        for qe in qs:
            if Ae[qe[1] - 1] - Ae[qe[0] - 1] == qe[2]:
                t0 += qe[3]
        r = max(r, t0)
    print(r)


def __starting_point():
    main()


__starting_point()
