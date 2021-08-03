N, M = list(map(int, input().split()))
A = list(list(input()) for _ in range(N))
B = list(list(input()) for _ in range(M))
flag = False
for i in range(0, N - M + 1):
    for j in range(0, N - M + 1):
        sub = True
        for x in range(0, M):
            for y in range(0, M):
                if A[i + x][j + y] != B[x][y]:
                    sub = False
        flag = flag or sub
if flag:
    print("Yes")
else:
    print("No")
