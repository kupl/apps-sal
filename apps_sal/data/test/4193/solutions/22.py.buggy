A = [[int(i) for i in input().split()] for j in range(3)]
N = int(input())
b = [int(input()) for i in range(N)]
for i in range(N):
    for j in range(3):
        for k in range(3):
            if(b[i] == A[j][k]):
                A[j][k] = 0
for i in range(3):
    if(A[i][0] == A[i][1] and A[i][1] == A[i][2]):
        print("Yes")
        return
    if(A[0][i] == A[1][i] and A[1][i] == A[2][i]):
        print("Yes")
        return
if(A[0][0] == A[1][1] and A[1][1] == A[2][2]):
    print("Yes")
    return
if(A[0][2] == A[1][1] and A[1][1] == A[2][0]):
    print("Yes")
    return
print("No")
