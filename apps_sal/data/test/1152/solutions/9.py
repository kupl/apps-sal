N, M = list(map(int, input().split()))
A = [[int(a) for a in input().split()] for i in range(N)]
B = [[int(a) for a in input().split()] for i in range(N)]
C = [[A[i][j] ^ B[i][j] for j in range(M)] for i in range(N)]

for i in range(N):
    if sum(C[i]) % 2:
        print("No")
        break
    if i < N - 1:
        for j in range(M):
            C[i + 1][j] ^= C[i][j]

else:
    if sum(C[N - 1]) == 0:
        print("Yes")
    else:
        print("No")
