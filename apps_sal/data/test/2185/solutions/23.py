from itertools import groupby
T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = []
    for (a, b) in zip(A, B):
        C.append(b - a)
    D = []
    for (v, g) in groupby(C):
        D.append(v)
    if len(D) == 1:
        if D[0] >= 0:
            print('YES')
        else:
            print('NO')
    elif len(D) == 2:
        if 0 in D:
            D.remove(0)
            if D[0] >= 0:
                print('YES')
            else:
                print('NO')
        else:
            print('NO')
    elif len(D) == 3:
        if D[0] == D[-1] == 0 and D[1] >= 0:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')
