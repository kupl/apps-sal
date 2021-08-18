
def INT(): return int(input())


def INTM(): return map(int, input().split())
def STRM(): return map(str, input().split())
def STR(): return str(input())


def LIST(): return list(map(int, input().split()))
def LISTS(): return list(map(str, input().split()))


def do():
    n = INT()
    A = []
    for i in range(n):
        A.append(INT())

    B = sorted(A, reverse=True)
    m1 = A.count(B[0])
    m2 = A.count(B[1])
    if m1 >= 2:
        flg = True
    else:
        index = A.index(B[0])
        flg = False

    if flg:
        for i in range(n):
            print(B[0])
    else:
        for i in range(n):
            if i != index:
                print(B[0])
            else:
                print(B[1])


def __starting_point():
    do()


__starting_point()
