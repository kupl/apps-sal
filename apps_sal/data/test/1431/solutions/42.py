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


def Main():
    n = read_int()
    a = read_int_list()
    b = [0] * n
    ans = []
    for i in range(n - 1, -1, -1):
        if sum(b[i::i + 1]) % 2 != a[i]:
            b[i] = 1
            ans.append(i + 1)
    print(len(ans))
    if len(ans):
        print(*ans)


def __starting_point():
    Main()


__starting_point()
