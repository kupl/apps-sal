from functools import lru_cache
import sys


def rs():
    return sys.stdin.readline().rstrip()


def ri():
    return int(sys.stdin.readline())


def ria():
    return list(map(int, sys.stdin.readline().split()))


def ws(s):
    sys.stdout.write(s)
    sys.stdout.write('\n')


def wi(n):
    sys.stdout.write(str(n))
    sys.stdout.write('\n')


def wia(a, sep=' '):
    sys.stdout.write(sep.join([str(x) for x in a]))
    sys.stdout.write('\n')


def solve(n, m, a):
    b = [[] for _ in range(m)]
    for j in range(m):
        for (l, r, i) in a:
            if l <= j <= r:
                b[j].append((l, r, i))

    @lru_cache(maxsize=None)
    def go(left, right):
        if left > right:
            return 0
        best = 0
        for mid in range(left, right + 1):
            cnt = 0
            for (l, r, i) in b[mid]:
                if l <= mid <= r and l >= left and (r <= right):
                    cnt += 1
            best = max(best, cnt * cnt + go(left, mid - 1) + go(mid + 1, right))
        return best
    return go(0, m - 1)


def main():
    (n, m) = ria()
    a = set()
    for i in range(n):
        k = ri()
        for j in range(k):
            (l, r) = ria()
            l -= 1
            r -= 1
            a.add((l, r, i))
    wi(solve(n, m, a))


def __starting_point():
    main()


__starting_point()
