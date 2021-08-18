def main():
    n, k = list(map(int, input().split()))
    p = list(map(int, input().split()))
    solve(n, k, p)


def solve(n, k, p):
    group = 256 * [None]
    r = p[:]
    for i, pi in enumerate(p):
        if group[pi] is not None:
            r[i] = group[pi][0]
        else:
            lo = pi
            while lo >= 0 and pi - lo < k and group[lo] is None:
                lo -= 1
            if lo < 0 or pi - lo == k:
                lo += 1
                hi = pi + 1
            else:
                if pi - group[lo][0] < k:
                    lo = group[lo][0]
                    hi = pi + 1
                else:
                    lo += 1
                    hi = pi + 1
            lohi = (lo, hi)
            for j in range(lo, hi):
                group[j] = lohi
            r[i] = group[pi][0]
    print(" ".join(map(str, r)))


main()
