import sys
from bisect import bisect_left, bisect_right


def binom(n, k):
    if k > n:
        return 0
    elif k == 0:
        return 1
    elif k == 1:
        return n
    elif k == 2:
        return (n * (n - 1)) // 2
    elif k == 3:
        return (n * (n - 1) * (n - 2)) // 6
    else:
        raise NotImplementedError


def ways_to_pick(xs, wx, lo, hi):
    idx_lo = bisect_left(xs, lo)
    idx_hi = bisect_right(xs, hi)
    return binom(idx_hi - idx_lo, wx)


def number_of_teams(gs, wg, ds, wd, fs, wf, lo, hi):
    return ways_to_pick(gs, wg, lo, hi) * \
        ways_to_pick(ds, wd, lo, hi) * \
        ways_to_pick(fs, wf, lo, hi)


ng, nd, nf = list(map(int, input().split()))
gs = list(sorted(map(int, input().split())))
ds = list(sorted(map(int, input().split())))
fs = list(sorted(map(int, input().split())))

wg = 1
wd = 2
wf = 3

if nd < 2 or nf < 3:
    print(0)
    return

ans = 0
for idx, min_el in enumerate(gs):
    ans += number_of_teams(gs[idx + 1:], wg - 1,
                           ds, wd,
                           fs, wf,
                           min_el, 2 * min_el)
for idx, min_el in enumerate(ds):
    ans += number_of_teams(gs, wg,
                           ds[idx + 1:], wd - 1,
                           fs, wf,
                           min_el, 2 * min_el)
for idx, min_el in enumerate(fs):
    ans += number_of_teams(gs, wg,
                           ds, wd,
                           fs[idx + 1:], wf - 1,
                           min_el, 2 * min_el)
print(ans)
