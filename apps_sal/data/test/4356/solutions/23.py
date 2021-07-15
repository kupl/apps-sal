N, M = list(map(int, input().split()))
A = []
B = []
for i in range(N):
    A.append(input())
for i in range(M):
    B.append(input())

for i in range(N-M+1):
    if B[0] in A[i]:
        k = A[i].index(B[0])
        points = 1
        for j in range(1,M):
            if B[j] == A[i+j][k:k+M]:
                points += 1
        if points == M:
            print('Yes')
            return
print('No')

