import numpy as np


def INT():
    return int(input())


def INTM():
    return map(int, input().split())


def STRM():
    return map(str, input().split())


def STR():
    return str(input())


def LIST():
    return list(map(int, input().split()))


def LISTS():
    return list(map(str, input().split()))


def do():
    n = INT()
    a = np.array(LIST())
    ans = 0
    mod = 10 ** 9 + 7
    for i in range(70):
        digit = np.sum(a >> i & 1)
        ans += pow(2, i, mod) * ((n - digit) * digit % mod) % mod
        ans = ans % mod
    print(ans)


def __starting_point():
    do()


__starting_point()
