N = int(input())
if N <= 5:
    A = [[0] * N for _ in range(N)]
    A[0] = list(map(int, input().split()))
    for i in range(1, N):
        A[i][0] = int(input())
    for i in range(1, N):
        for j in range(1, N):
            lis = [0] * 3
            lis[A[i - 1][j]] = 1
            lis[A[i][j - 1]] = 1
            for k in range(3):
                if lis[k] == 0:
                    A[i][j] = k
                    break
    lis = [0] * 3
    for i in range(N):
        for j in range(N):
            lis[A[i][j]] += 1
else:
    A = [[0] * N for _ in range(4)]
    A[0] = list(map(int, input().split()))
    B = [[0] * 4 for _ in range(N)]
    for i in range(1, N):
        B[i][0] = int(input())
    for i in range(1, 4):
        A[i][0] = B[i][0]
    for j in range(4):
        B[0][j] = A[0][j]

    for i in range(1, 4):
        for j in range(1, N):
            lis = [0] * 3
            lis[A[i - 1][j]] = 1
            lis[A[i][j - 1]] = 1
            for k in range(3):
                if lis[k] == 0:
                    A[i][j] = k
                    break
    for i in range(1, N):
        for j in range(1, 4):
            lis = [0] * 3
            lis[B[i - 1][j]] = 1
            lis[B[i][j - 1]] = 1
            for k in range(3):
                if lis[k] == 0:
                    B[i][j] = k
                    break
    lis = [0] * 3
    for i in range(3):
        for j in range(N):
            lis[A[i][j]] += 1
    for i in range(3, N):
        for j in range(3):
            lis[B[i][j]] += 1
    for j in range(3, N):
        lis[A[3][j]] += N - j
    for i in range(4, N):
        lis[B[i][3]] += N - i
print((*lis))
