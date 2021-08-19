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
    ans = [0] * n
    rain = sum(A)
    temp = rain
    for i in range(n):
        if i % 2 == 1:
            temp -= A[i] * 2
    ans[0] = temp
    for i in range(1, n):
        ans[i] = A[i - 1] * 2 - ans[i - 1]
    print(*ans)


def __starting_point():
    do()


__starting_point()
