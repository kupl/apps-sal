import sys
sys.setrecursionlimit(10 ** 5)


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


for _ in range(II()):
    (x, y, k) = MI()
    a = (k * (y + 1) - 1 + x - 2) // (x - 1)
    print(a + k)
