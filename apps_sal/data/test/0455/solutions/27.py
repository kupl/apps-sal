import math
N = int(input())
XY = []
for i in range(N):
    XY.append(list(map(int, input().split())))
mr = abs(XY[0][0]) + abs(XY[0][1])
for i in range(1, N):
    if abs(XY[i][0]) + abs(XY[i][1]) > mr:
        mr = abs(XY[i][0]) + abs(XY[i][1])
m = int(math.log(mr, 2) // 1 + 1)
g = (XY[0][0] + XY[0][1]) % 2
cnt = 0
for i in range(N):
    if (XY[i][0] + XY[i][1]) % 2 == g:
        cnt += 1
if cnt != N:
    print(-1)
else:
    if g == 1:
        W = [''] * N
        for i in range(N):
            for j in range(m):
                if abs(XY[i][0]) >= abs(XY[i][1]) and XY[i][0] >= 0:
                    W[i] += 'R'
                    XY[i][0] -= 2**(m - j - 1)
                elif abs(XY[i][0]) >= abs(XY[i][1]) and XY[i][0] < 0:
                    W[i] += 'L'
                    XY[i][0] += 2**(m - j - 1)
                elif abs(XY[i][0]) < abs(XY[i][1]) and XY[i][1] >= 0:
                    W[i] += 'U'
                    XY[i][1] -= 2**(m - j - 1)
                elif abs(XY[i][0]) < abs(XY[i][1]) and XY[i][1] < 0:
                    W[i] += 'D'
                    XY[i][1] += 2**(m - j - 1)
        print(m)
        for i in range(m):
            print(2**i, end=' ')
        print()
        for j in range(N):
            print(W[j][::-1])
    else:
        for i in range(N):
            XY[i][0] += 1
        W = [''] * N
        for i in range(N):
            for j in range(m):
                if abs(XY[i][0]) >= abs(XY[i][1]) and XY[i][0] >= 0:
                    W[i] += 'R'
                    XY[i][0] -= 2**(m - j - 1)
                elif abs(XY[i][0]) >= abs(XY[i][1]) and XY[i][0] < 0:
                    W[i] += 'L'
                    XY[i][0] += 2**(m - j - 1)
                elif abs(XY[i][0]) < abs(XY[i][1]) and XY[i][1] >= 0:
                    W[i] += 'U'
                    XY[i][1] -= 2**(m - j - 1)
                elif abs(XY[i][0]) < abs(XY[i][1]) and XY[i][1] < 0:
                    W[i] += 'D'
                    XY[i][1] += 2**(m - j - 1)
        print(m + 1)
        print(1, end=' ')
        for i in range(m):
            print(2**i, end=' ')
        print()
        for j in range(N):
            W[j] += 'L'
            print(W[j][::-1])
