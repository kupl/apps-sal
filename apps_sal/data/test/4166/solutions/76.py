def main():
    (N, M) = list(map(int, input().split()))
    A = [-1] * N
    tmp = ''
    flg = True
    for i in range(M):
        (s, c) = list(map(int, input().split()))
        if A[s - 1] == -1:
            A[s - 1] = c
        elif A[s - 1] != c:
            flg = False
    for i in range(N):
        if i == 0 and N > 1:
            if A[i] == -1:
                tmp += '1'
            elif A[i] == 0:
                flg = False
                break
            else:
                tmp += str(A[i])
        elif A[i] == -1:
            tmp += '0'
        else:
            tmp += str(A[i])
    print(int(tmp) if flg else -1)


def __starting_point():
    main()


__starting_point()
