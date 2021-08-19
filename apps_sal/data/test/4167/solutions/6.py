import sys
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


def lcm(a: int, b: int) -> int:
    return a * b // math.gcd(a, b)


def Main():
    (n, k) = read_ints()
    if k % 2:
        print((n // k) ** 3)
    else:
        print((n // k) ** 3 + ((n + k // 2) // k) ** 3)


def __starting_point():
    Main()


__starting_point()
