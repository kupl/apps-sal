import sys
sys.setrecursionlimit(10 ** 6)


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


def gcd(a, b):
    while b:
        (a, b) = (b, a % b)
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


def main():
    n = II()
    ta = LLI(n)
    x = y = -1
    for (t, a) in ta:
        if x == -1:
            (x, y) = (t, a)
            continue
        c = max((t + x - 1) // t, (a + y - 1) // a)
        x = c * t
        y = c * a
    print(x + y)


main()
