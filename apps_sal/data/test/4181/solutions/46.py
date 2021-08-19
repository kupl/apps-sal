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
    A = LIST()
    B = LIST()
    ans = 0
    ta = A[0]
    for i in range(n):
        tb = B[i]
        ans += min(ta, tb)
        (ta, tb) = (max(0, ta - tb), max(0, tb - ta))
        ta += A[i + 1]
        ans += min(ta, tb)
        ta = max(0, ta - tb)
        ta = min(ta, A[i + 1])
    print(ans)


def __starting_point():
    do()


__starting_point()
