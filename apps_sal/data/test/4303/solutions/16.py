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


def read_str_list():
    return list(sys.stdin.readline().strip().split())


def read_int_list():
    return list(map(int, sys.stdin.readline().strip().split()))


def lcm(a: int, b: int) -> int:
    return a * b // math.gcd(a, b)


def Main():
    (n, k) = read_ints()
    x = read_int_list()
    ans = INF
    for i in range(n - k + 1):
        left = x[i]
        right = x[i + k - 1]
        if left < 0 and right > 0:
            ans = min(ans, min(abs(left), abs(right)) * 2 + max(abs(left), abs(right)))
        else:
            ans = min(ans, max(abs(left), abs(right)))
    print(ans)


def __starting_point():
    Main()


__starting_point()
