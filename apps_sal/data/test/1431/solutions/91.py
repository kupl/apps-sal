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
    flg = True
    la = len(A)
    bool = [False] * (n + 1)
    B = []
    for i in range(la - 1, -1, -1):
        a = A[i]
        s = i + 1
        temp = 0
        for j in range(n // s + 1):
            if j == 0:
                continue
            if bool[j * s]:
                temp += 1
        if temp % 2 != a:
            B.append(s)
            bool[s] = True
    B = sorted(B)
    print(len(B))
    if len(B) != 0:
        print(*B)


def __starting_point():
    do()


__starting_point()
