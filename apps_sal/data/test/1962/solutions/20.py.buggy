import sys
import math
import os.path

FILE_INPUT = "C.in"
DEBUG = os.path.isfile(FILE_INPUT)
if DEBUG:
    sys.stdin = open(FILE_INPUT)


def ni():
    return list(map(int, input().split(" ")))


def nia():
    return list(map(int, input().split()))


def log(x):
    if (DEBUG):
        print(x)


n, k, l = ni()
a = nia()
# print(n,k,l)
log(a)

vmin = min(a)
log(vmin)

if (n == 1):
    print(vmin)
    return

vmaxa = vmin + l
log(vmaxa)
amax = [i for i in a if i <= vmaxa]
log(f"{amax} -> {len(amax)}")

if (len(amax) < n):
    print(0)

else:
    amax.sort()
    log(amax)
    ans = 0
    count = 0
    lonhonMax = n * k - len(amax)
    for i in amax[0::k]:
        log(f"+ {count*k}: {i}")
        ans += i
        count += 1
        if (count == n):
            break

    if (count < n):
        ix = len(amax) - 1
        log(f"add more={n} - {count} = {n - count}")
        for i in range(n - count):
            if (ix % k == 0):
                ix -= 1
            ans += amax[ix]
            ix -= 1
    print(ans)
