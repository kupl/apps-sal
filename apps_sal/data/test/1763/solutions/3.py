import sys
import bisect
readline = sys.stdin.readline
readall = sys.stdin.read


def ns():
    return readline().rstrip()


def ni():
    return int(readline().rstrip())


def nm():
    return map(int, readline().split())


def nl():
    return list(map(int, readline().split()))


def prn(x):
    return print(*x, sep='\n')


def solve():
    (n, a, r, m) = nm()
    hl = nl()
    shl = [0] * (n + 1)
    hl.sort()
    for i in range(n):
        shl[i + 1] = shl[i] + hl[i]

    def cost(x):
        lidx = bisect.bisect_left(hl, x)
        ridx = bisect.bisect_right(hl, x)
        much = shl[-1] - shl[ridx] - x * (n - ridx)
        less = x * lidx - shl[lidx]
        res = min(m, a + r) * min(much, less)
        if much > less:
            res += r * (much - less)
        else:
            res += a * (less - much)
        return res
    (lo, hi) = (min(hl) - 1, max(hl) + 1)
    while hi - lo > 3:
        mlo = (hi + lo * 2) // 3
        mhi = (hi * 2 + lo) // 3
        if cost(mlo) < cost(mhi):
            hi = mhi
        else:
            lo = mlo
    print(min((cost(i) for i in range(lo, hi + 1))))
    return


solve()
