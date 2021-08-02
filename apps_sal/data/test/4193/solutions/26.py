A = [0 for i in range(9)]
for i in range(3):
    A[3 * i], A[3 * i + 1], A[3 * i + 2] = map(int, input().split())
N = int(input())
b = [0 for i in range(N)]
for i in range(N):
    b[i] = int(input())

# Check matching numbers
for i in range(9):
    for j in range(N):
        if A[i] == b[j]:
            A[i] = 1

# Check bingo or not
flag = 0
# Check rows
for i in [0, 3, 6]:
    if A[i] == A[i + 1] and A[i + 1] == A[i + 2]:
        flag += 1
# Check colums
for j in range(3):
    if A[j] == A[j + 3] and A[j + 3] == A[j + 6]:
        flag += 1
# Check naname?
if (A[0] == A[4] and A[4] == A[8]) or (A[2] == A[4] and A[4] == A[6]):
    flag += 1

if flag >= 1:
    print("Yes")
else:
    print("No")
