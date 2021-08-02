a = [int(c) for c in input().split()]
N = a[0]
M = a[1]
C = a[2]
B = [int(c) for c in input().split()]
A = [list(map(int, input().split())) for c in range(N)]

result = []

for i in range(N):
    cnt = C
    for j in range(M):
        cnt += A[i][j] * B[j]

    if cnt > 0:
        result.append(1)
    else:
        result.append(0)

print(sum(result))
