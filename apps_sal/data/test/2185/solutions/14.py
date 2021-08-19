import sys


def minp():
    return sys.stdin.readline().strip()


def mint():
    return int(minp())


def mints():
    return list(map(int, minp().split()))


def solve():
    n = mint()
    a = list(mints())
    b = list(mints())
    diff = None
    last = 0
    for i in range(n):
        if b[i] != a[i]:
            last = i
    for i in range(n):
        d = b[i] - a[i]
        if diff != None and i <= last and (d != diff):
            return False
        if d != 0:
            if d < 0:
                return False
            diff = d
    return True


for i in range(mint()):
    print(['NO', 'YES'][solve()])
