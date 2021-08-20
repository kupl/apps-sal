N = int(input())
A = []
XY = []
for i in range(N):
    a = int(input())
    A.append(a)
    xy = [list(map(int, input().split())) for j in range(a)]
    XY.append(xy)
ans = 0
for i in range(2 ** N):
    b = [i >> j & 1 for j in range(N)]
    f = 0
    for j in range(N):
        if b[j] == 1:
            for k in range(A[j]):
                x = XY[j][k][0] - 1
                y = XY[j][k][1]
                if b[x] != y:
                    f = 1
                    break
        if f:
            break
    else:
        ans = max(ans, b.count(1))
print(ans)
