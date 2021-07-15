def __starting_point():

    n,k = list(map(int,input().split()))
    A = [0]
    AA= list(map(int,input().split()))
    A = A + AA

    B = set()
    cnt = 0
    ind = 1
    startind = 0
    D = []
    while True:
        if A[ind] not in B:
            B.add(ind)
            D.append(ind)
            cnt += 1
            ind = A[ind]
        else:
            B.add(ind)
            D.append(ind)
            cnt += 1
            startind = A[ind]
            break

    C = set()
    ind = startind
    ANS = []
    while True:
        if A[ind] not in C:
            C.add(ind)
            ind = A[ind]
            ANS.append(ind)
        else:
            C.add(ind)
            ANS.append(A[ind])
            break

    if k >= cnt:
        tmp = k - cnt
        tmp = tmp % (len(C))
        print((ANS[tmp-1]))
    else:
        print((D[k]))

__starting_point()
