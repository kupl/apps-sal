import sys


def IS():
    return sys.stdin.readline().rstrip()


def II():
    return int(IS())


def MII():
    return list(map(int, IS().split()))


def MIIZ():
    return list(map(lambda x: x - 1, MII()))


INIT_VAL = 0


def MD2(d1, d2):
    return [[INIT_VAL] * d2 for _ in range(d1)]


def MD3(d1, d2, d3):
    return [MD2(d2, d3) for _ in range(d1)]


def DIVC(x, y):
    return -(-x // y)


def DIVF(x, y):
    return x // y


def main():
    (n, p) = MII()
    s = list(map(int, IS()))
    if 10 % p == 0:
        cnt = 0
        for (i, si) in enumerate(s):
            if si % p == 0:
                cnt += i + 1
        print(cnt)
        return None
    d = [0] * p
    d[0] = 1
    ss = 0
    x = 1
    for si in s[::-1]:
        ss += x * si
        ss %= p
        d[ss] += 1
        x = 10 * x % p
    cnt = 0
    for di in d:
        cnt += di * (di - 1) // 2
    print(cnt)


def __starting_point():
    main()


__starting_point()
