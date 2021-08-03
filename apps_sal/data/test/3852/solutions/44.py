N = int(input())
A = list(map(int, input().split()))
flag = 0
for i in range(N):
    if A[i] != 0:
        flag = 1
        break
if flag == 0:
    print(0)
else:
    pmax = 0
    mmin = 0
    indp = -1
    indm = -1
    for i in range(N):
        if A[i] > 0:
            if A[i] > pmax:
                pmax = A[i]
                indp = i
        elif A[i] < 0:
            if A[i] < mmin:
                mmin = A[i]
                indm = i
    if pmax >= abs(mmin):
        print(2 * N - 2)
        for i in range(N):
            if i != indp:
                print(indp + 1, i + 1)
        for i in range(N - 1):
            print(i + 1, i + 2)
    else:
        print(2 * N - 2)
        for i in range(N):
            if i != indm:
                print(indm + 1, i + 1)
        for i in range(N - 1, 0, -1):
            print(i + 1, i)
