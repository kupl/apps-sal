import sys
N, M = list(map(int, input().split()))
A = []
B = []
for _ in range(N):
    A.append(input())
for _ in range(M):
    B.append(input())

for i in range(N-M+1):
    for j in range(N-M+1):
        for k in range(M):
            #print(A[i+k][j:j+M])
            #print(B[k])
            if A[i+k][j:j+M] != B[k]:
                break
        else:
            print("Yes")
            return
print("No")


