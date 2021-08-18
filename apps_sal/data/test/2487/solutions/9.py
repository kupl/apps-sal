

def solve(ls, debug=0):
    n = len(ls) + 1
    term1 = ((n + 2) * (n + 1) * n) // 6
    term2 = 0
    for i, j in ls:
        if i > j:
            i, j = j, i
        term2 += i * (n + 1 - j)

    return term1 - term2


def main(istr, ostr):
    n = int(istr.readline())
    ls = []
    for i in range(n - 1):
        v1, v2 = list(map(int, istr.readline().strip().split()))
        ls.append([v1, v2])
    result = solve(ls)
    print(result, file=ostr)


def __starting_point():
    import sys

    main(sys.stdin, sys.stdout)


__starting_point()
