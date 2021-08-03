import sys
a = 3
A = [list(map(int, input().split())) for c in range(a)]
N = int(input())
b = [int(input()) for c in range(N)]
# print(A)
# print(b)
C = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(3):
    for j in range(3):
        for k in range(N):
            if b[k] == A[i][j]:
                C[i][j] = 1

for i in range(3):
    if sum(C[i]) == 3:
        print("Yes")
        return

for j in range(3):
    if C[0][j] + C[1][j] + C[2][j] == 3:
        print("Yes")
        return

if C[0][0] + C[1][1] + C[2][2] == 3 or C[0][2] + C[1][1] + C[2][0] == 3:
    print("Yes")
    return

print("No")
