import sys


def int1(x):
    return int(x) - 1


def p2D(x):
    return print(*x, sep='\n')


def II():
    return int(sys.stdin.readline())


def MI():
    return map(int, sys.stdin.readline().split())


def LI():
    return list(map(int, sys.stdin.readline().split()))


def LLI(rows_number):
    return [LI() for _ in range(rows_number)]


def SI():
    return sys.stdin.readline()[:-1]


def main():
    n = II()
    aa = LI()
    x = 0
    for a in aa[2:]:
        x ^= a
    t = aa[0] + aa[1] - x
    if t < 0 or t & 1:
        print(-1)
        return
    t >>= 1
    a0 = a1 = 0
    for i in range(40, -1, -1):
        dt = t >> i & 1
        dx = x >> i & 1
        if (dt, dx) == (1, 1):
            print(-1)
            return
        if (dt, dx) == (1, 0):
            a0 |= 1 << i
            a1 |= 1 << i
    for i in range(40, -1, -1):
        dt = t >> i & 1
        dx = x >> i & 1
        if (dt, dx) == (0, 1):
            if a0 | 1 << i <= aa[0]:
                a0 |= 1 << i
            else:
                a1 |= 1 << i
    if a0 > 0 and a0 <= aa[0]:
        print(aa[0] - a0)
    else:
        print(-1)


main()
