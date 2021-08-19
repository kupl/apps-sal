# Function to rotate the matrix
# 90 degree clockwise
def rotate90Clockwise(A):
    N = len(A[0])
    for i in range(N // 2):
        for j in range(i, N - i - 1):
            temp = A[i][j]
            A[i][j] = A[N - 1 - j][i]
            A[N - 1 - j][i] = A[N - 1 - i][N - 1 - j]
            A[N - 1 - i][N - 1 - j] = A[j][N - 1 - i]
            A[j][N - 1 - i] = temp


def check(A, B):
    c1 = 0
    c2 = 0
    for i in range(N):
        for j in range(N):
            if(A[i][j] == B[N - 1 - i][j]):
                c1 += 1
            if(A[i][j] == B[i][N - 1 - j]):
                c2 += 1
    if(c1 == N**2 or c2 == N**2):
        return True
    else:
        return False


N = int(input())
A = []
for i in range(N):
    a = input()
    aa = []
    for j in range(N):
        aa.append(a[j])
    A.append(aa)
B = []
for j in range(N):
    b = input()
    bb = []
    for j in range(N):
        bb.append(b[j])
    B.append(bb)
flag = False
if(A == B):
    flag = True
if(check(A, B)):
    flag = True
rotate90Clockwise(A)
if(A == B):
    flag = True
if(check(A, B)):
    flag = True
rotate90Clockwise(A)
if(A == B):
    flag = True
if(check(A, B)):
    flag = True
rotate90Clockwise(A)
if(A == B):
    flag = True
if(check(A, B)):
    flag = True
if(flag):
    print("Yes")
else:
    print("No")
