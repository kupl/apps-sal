N = int(input())
A = list(map(int, input().split()))
amax = 0
ind = -1
for i in range(N):
    if abs(A[i]) > amax:
        amax = abs(A[i])
        ind = i
if amax == 0:
    print(0)
else:
    m = 2 * N - 2
    B = []
    if A[ind] >= 0:
        for i in range(N):
            if i != ind:
                B.append((ind + 1, i + 1))
        for i in range(N - 1):
            B.append((i + 1, i + 2))
    else:
        for i in range(N):
            if i != ind:
                B.append((ind + 1, i + 1))
        for i in range(N, 1, -1):
            B.append((i, i - 1))
    print(m)
    for i in range(m):
        print(B[i][0], B[i][1])
