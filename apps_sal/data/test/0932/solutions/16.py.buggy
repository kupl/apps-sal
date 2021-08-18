m, n = map(int, input().split())
B = [list(map(int, input().split())) for x in range(m)]
A = [[1 for x in range(n)] for x in range(m)]
#C = [[0 for x in range(n)] for x in range(m)]
for i in range(m):
    for j in range(n):
        if B[i][j] == 0:
            for y in range(m):
                A[y][j] = 0
            for z in range(n):
                A[i][z] = 0
for i in range(m):
    for j in range(n):
        tmp = 0
        for y in range(m):
            tmp = tmp | A[y][j]
        for z in range(n):
            tmp = tmp | A[i][z]
        if tmp != B[i][j]:
            print("NO")
            return
print("YES")
for li in A:
    print(' '.join(map(str, li)))
