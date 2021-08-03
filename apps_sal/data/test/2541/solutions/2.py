import math
import bisect
import sys


def flrt(exp, x):
    l = max(0, math.floor(x**(1 / exp)) - 3)

    r = math.floor(x**(1 / exp)) + 3
    while l < r:
        mid = (l + r) // 2
        if mid**exp <= x:
            l = mid + 1
        else:
            r = mid
    return l - 1


def c1(r):
    ans = set()
    pr = [5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61]
    for i in pr:
        x = 2
        while x**i <= r:
            val = x**i
            b2 = flrt(2, val)
            b3 = flrt(3, val)
            if b2**2 != val and b3**3 != val:
                ans.add(val)
            x += 1
    return ans


def solve(r, pc):
    if r == 0:
        return 0

    a = [2, 3]
    ans = 0
    for i in range(1, 2**len(a)):
        tot = 0
        mult = 1
        for j, x in enumerate(a):
            if i & (1 << j):
                mult *= x
                tot += 1
        d = flrt(mult, r)
        ans += d if tot % 2 else -d

    return ans + bisect.bisect_right(pc, r)

    lp = 0
    rp = len(pc)
    while lp < rp:
        mid = (lp + rp) // 2
        if pc[mid] <= r:
            lp = mid + 1
        else:
            rp = mid

    return ans + lp


q = int(input())

pc = c1(1e18 + 1)


pca = list(pc)
pca.sort()


for i in range(q):
    l, r = [int(x) for x in sys.stdin.readline().split()]
    ans = solve(r, pca) - solve(l - 1, pca)
    sys.stdout.write(str(ans) + '\n')
