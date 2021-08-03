import sys


def minp():
    return sys.stdin.readline().strip()


def mint():
    return int(minp())


def mints():
    return list(map(int, minp().split()))


def solve():
    a = list(mints())
    a.sort()
    if a[-1] != a[-2]:
        print("NO")
        return
    else:
        print("YES")
        print(a[0], a[0], a[1])


for i in range(mint()):
    solve()
