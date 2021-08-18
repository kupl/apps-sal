N, M = map(int, input().split())

A = []
for i in range(N):
    A.append(input())

B = []
for i in range(M):
    B.append(input())

for i in range(N - M + 1):
    for j in range(N - M + 1):
        for k in range(M):
            if A[i + k][j:j + M] != B[k]:
                break
            if k == M - 1:
                print("Yes")
                return

print("No")
