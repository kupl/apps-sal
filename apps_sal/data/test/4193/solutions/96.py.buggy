A = [list(map(int, input().split())) for i in range(3)]
n = int(input())
B = [int(input()) for i in range(n)]
C = [[0, 0, 0] for _ in range(3)]

for b in B:
    for i in range(3):
        for j in range(3):
            if(A[i][j] == b):
                C[i][j] = 1

for i in range(3):
    if(C[i][0] == 1 and C[i][1] == 1 and C[i][2] == 1):
        print("Yes")
        return
    elif(C[0][i] == 1 and C[1][i] == 1 and C[2][i] == 1):
        print("Yes")
        return
if(C[0][0] == 1 and C[1][1] == 1 and C[2][2] == 1):
    print("Yes")
    return
elif(C[0][2] == 1 and C[1][1] == 1 and C[2][0] == 1):
    print("Yes")
    return
print("No")
return
