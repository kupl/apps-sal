import sys
import math
MOD = 10 ** 9 + 7
INF = 10 ** 9
PI = 3.141592653589793


def read_str():
    return sys.stdin.readline().strip()


def read_int():
    return int(sys.stdin.readline().strip())


def read_ints():
    return map(int, sys.stdin.readline().strip().split())


def read_ints2(x):
    return map(lambda num: int(num) - x, sys.stdin.readline().strip().split())


def read_str_list():
    return list(sys.stdin.readline().strip().split())


def read_int_list():
    return list(map(int, sys.stdin.readline().strip().split()))


def GCD(a: int, b: int) -> int:
    return b if a % b == 0 else GCD(b, a % b)


def LCM(a: int, b: int) -> int:
    return a * b // GCD(a, b)


def Main():
    (n, m) = read_ints()
    a = read_int_list()
    a = [x // 2 for x in a]
    lcm = 1
    for x in a:
        lcm *= x // math.gcd(lcm, x)
    for x in a:
        if lcm // x % 2 == 0:
            print(0)
            return
    print(math.ceil(m // lcm / 2))


def __starting_point():
    Main()


__starting_point()
