N = int(input())
A = [0 for n in range(N)]
XY = [0 for n in range(N)]
count_max = 0
for i in range(N):
    A[i] = int(input())
    xy = []
    for j in range(A[i]):
        x_y = list(map(int, input().split()))
        xy.append(x_y)
    XY[i] = xy
for i in range(2 ** N):
    op = [0] * N
    for j in range(N):
        if i >> j & 1:
            op[N - 1 - j] = 1
    flag = True
    for k in range(len(op)):
        if op[k] == 1:
            for l in range(A[k]):
                if XY[k][l][1] != op[XY[k][l][0] - 1]:
                    flag = False
    if flag:
        if sum(op) > count_max:
            count_max = sum(op)
print(count_max)
