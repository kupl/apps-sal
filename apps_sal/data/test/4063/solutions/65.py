
def INT(): return int(input())


def INTM(): return map(int, input().split())
def STRM(): return map(str, input().split())
def STR(): return str(input())


def LIST(): return list(map(int, input().split()))
def LISTS(): return list(map(str, input().split()))


def do():
    n = INT()
    A = LIST()
    A = sorted(A)
    print(A[n // 2] - A[n // 2 - 1])


def __starting_point():
    do()


__starting_point()
