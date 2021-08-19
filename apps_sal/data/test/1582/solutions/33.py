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


def GCD(a: int, b: int) -> int:
    return b if a % b == 0 else GCD(b, a % b)


def LCM(a: int, b: int) -> int:
    return a * b // GCD(a, b)


def f(num):
    front = num
    back = num
    while front >= 10:
        front //= 10
    while back >= 10:
        back %= 10
    return (front, back)


def Main():
    n = read_int()
    cnt = [[0] * 10 for _ in range(10)]
    for x in range(1, n + 1):
        (front, back) = f(x)
        cnt[front][back] += 1
    ans = 0
    for x in range(10):
        for y in range(10):
            ans += cnt[x][y] * cnt[y][x]
    print(ans)


def __starting_point():
    Main()


__starting_point()
