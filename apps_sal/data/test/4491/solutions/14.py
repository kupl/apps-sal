N = int(input())
A = [list(map(int, input().split())) for i in range(2)]
B = [[0 for i in range(N)] for j in range(2)]
B[0][0] = A[0][0]
for i in range(2):
    for j in range(N):
        for (x, y) in [[0, -1], [-1, 0]]:
            id = i + x
            jd = j + y
            if id < 0 or id >= 2 or jd < 0 or (jd >= N):
                continue
            c = B[id][jd] + A[i][j]
            if c > B[i][j]:
                B[i][j] = c
print(B[1][N - 1])
