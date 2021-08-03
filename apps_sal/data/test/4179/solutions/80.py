N, M, C = list(map(int, input().split()))
B = list(map(int, input().split()))
A = [list(map(int, input().split())) for i in range(N)]
S = 0
for i in range(N):
    AB = 0
    for j in range(len(B)):
        AB += B[j] * A[i][j]
    if AB + C > 0:
        S += 1
print(S)
