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
    (n, m) = INTM()
    A = LIST()
    bcs = []
    for i in range(m):
        temp = LIST()
        bcs.append(temp)
    A = sorted(A)
    bcs = sorted(bcs, key=lambda x: x[1], reverse=True)
    itr = -1
    flg = False
    for (b, c) in bcs:
        if itr + b > n - 1:
            flg = True
        if flg:
            for i in range(itr + 1, n):
                if A[i] < c:
                    A[i] = c
                else:
                    itr = 10 ** 9
                    break
        elif A[itr + b] < c:
            A[itr + 1:itr + b + 1] = [c] * b
        else:
            for i in range(itr + 1, itr + b + 1):
                if A[i] < c:
                    A[i] = c
                else:
                    itr = 10 ** 9
                    break
        itr += b
        if itr > n - 1:
            break
    print(sum(A))


def __starting_point():
    do()


__starting_point()
