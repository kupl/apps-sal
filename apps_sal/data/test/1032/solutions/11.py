import copy
con = 10 ** 9 + 7
INF = float('inf')


def getlist():
    return list(map(int, input().split()))


def Binary_Search(N, P, A, dif):
    left = 0
    right = N - 1
    ansleft = dif
    ansright = -INF
    while left <= right:
        mid = (left + right) // 2
        jud = 'Yes'
        B = copy.deepcopy(A)
        B.append(INF)
        for t in range(N):
            B[t] -= mid
        array = [None] * N
        i = 0
        j = 0
        while True:
            if B[j] <= i:
                j += 1
            else:
                if (j - i) % P == 0:
                    jud = 'No'
                    break
                array[i] = j - i
                i += 1
            if i >= N:
                break
        if jud == 'Yes':
            ansright = max(ansright, dif + mid)
            left = mid + 1
        else:
            right = mid - 1
    return (ansleft, ansright)


def main():
    (N, P) = getlist()
    A = getlist()
    A = sorted(A)
    dif = 0
    for i in range(N):
        dif = max(dif, A[i] - i)
    for i in range(N):
        A[i] -= dif
    (L, R) = Binary_Search(N, P, A, dif)
    if R == -INF:
        print(0)
        print()
    else:
        Xlis = [i for i in range(L, R + 1)]
        print(len(Xlis))
        print(*Xlis)


def __starting_point():
    main()


__starting_point()
