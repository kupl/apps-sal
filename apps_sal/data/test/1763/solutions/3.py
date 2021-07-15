import sys
import bisect

readline = sys.stdin.readline
readall = sys.stdin.read
ns = lambda: readline().rstrip()
ni = lambda: int(readline().rstrip())
nm = lambda: map(int, readline().split())
nl = lambda: list(map(int, readline().split()))
prn = lambda x: print(*x, sep='\n')


def solve():
    n, a, r, m = nm()
    hl = nl()
    shl = [0]*(n+1)
    hl.sort()
    for i in range(n):
        shl[i+1] = shl[i] + hl[i]

    def cost(x):
        lidx = bisect.bisect_left(hl, x)
        ridx = bisect.bisect_right(hl, x)
        much = shl[-1] - shl[ridx] - x * (n - ridx)
        less = x * lidx - shl[lidx]
        # print(x, lidx, ridx, much, less)
        res = min(m, a+r) * min(much, less)
        if much > less:
            res += r * (much - less)
        else:
            res += a * (less - much)
        return res

    # print([cost(i) for i in range(10)])
    lo, hi = min(hl) - 1, max(hl) + 1
    while hi - lo > 3:
        mlo = (hi + lo*2)//3
        mhi = (hi*2 + lo)//3
        # print(mlo, cost(mlo))
        if cost(mlo) < cost(mhi):
            hi = mhi
        else:
            lo = mlo
    print(min(cost(i) for i in range(lo, hi+1)))
    return

solve()

# T = ni()
# for _ in range(T):
#     solve()

