import sys

def main():
    n, m = map(int, input().split())
    k = [int(x) for x in input().split()]

    d = [[] for _ in range(4 * 10**5 + 1)]
    for j in range(m):
        dj, tj = map(int, input().split())
        d[dj - 1].append(tj - 1)

    lo, hi = 0, 4 * 10**5 + 1
    while lo < hi:
        mi = (hi + lo) // 2
        cash = mi
        offset = 0

        _k = k[:]
        for i in reversed(range(mi)):
            for j in d[i]:
                while cash and _k[j]:
                    _k[j] -= 1
                    cash -= 1
            if cash == i + 1:
                cash -= 2
                offset += 1

        if 2 * (sum(_k) - offset) <= cash:
            hi = mi
        else:
            lo = mi + 1

    print(lo)

input = iter(sys.stdin.read().splitlines()).__next__

def __starting_point():
    main()
__starting_point()
