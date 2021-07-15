A = [list(map(int,input().split())) for i in range(3)]
N = int(input())
for i in range(N):
    b = int(input())
    for j in range(3):
        for k in range(3):
            if A[j][k] == b:
                A[j][k] = 0
ans = "No"
for i in range(3):
    if A[i] == [0,0,0]:
        ans = "Yes"
        break
    for j in range(3):
        if A[j][i] != 0:
            break
    else:
        ans = "Yes"
        break
for i in range(3):
    if A[i][i] != 0:
        break
else:
    ans = "Yes"
if A[0][2] == 0 and A[1][1] == 0 and A[2][0] == 0:
    ans = "Yes"
print(ans)
