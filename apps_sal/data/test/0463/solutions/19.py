import sys

n, x = list(map(int, input().split()))
A = list(map(int, input().split()))

A.sort()
check = 0
for i in range(1, n):
    if A[i] == A[i - 1]:
        check = 1
        break

if check == 1:
    print(0)
    return

B = [A[i] for i in range(n)]

for i in range(n):
    A[i] = A[i] & x

AX = [(A[i], i) for i in range(n)]

AX.sort()

check = 0
i = 0
j = 0
while i < n:
    if AX[i][0] == B[j]:
        if AX[i][1] != j:
            check = 1
            break
        else:
            i += 1
    elif AX[i][0] < B[j]:
        i += 1
    elif AX[i][0] > B[j]:
        j += 1

if check == 1:
    print(1)
    return


check = 0
for i in range(1, n):
    if AX[i][0] == AX[i - 1][0]:
        check = 1
        break

if check == 1:
    print(2)
    return

print(-1)
