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
    b = [True] * n
    for i in range(n - 1):
        j = i + 1
        z = (a[i], i)
        while j < n and b[j - 1]:
            z = min(z, (a[j], j))
            j += 1
        if z[0] < a[i]:
            j = z[1] - 1
            while j >= i:
                a[j], a[j + 1] = a[j + 1], a[j]
                b[j] = False
                j -= 1
    print(*a)


for i in range(mint()):
    solve()
