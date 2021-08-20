import sys


def LI():
    return [int(x) for x in sys.stdin.readline().split()]


def solve():
    (n, p) = LI()
    a = LI()
    a.sort()
    ap = [i for i in a[p - 1:]]
    ap = [ap[i] - i for i in range(len(ap))]
    M = min(ap)
    b = [a[i] - i for i in range(n)]
    m = max(b)
    ans = list(range(m, M))
    print(len(ans))
    print(*ans)
    return


def __starting_point():
    solve()


__starting_point()
