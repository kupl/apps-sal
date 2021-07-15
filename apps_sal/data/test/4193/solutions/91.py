A = [list(map(int, input().split())) for _ in range(3)]
n = int(input())
B = [int(input()) for _ in range(n)]

for i in range(3):
    for j in range(3):
        if A[i][j] in B:
            A[i][j] = -1

for i in range(3):
    ans1, ans2 = 0, 0
    for j in range(3):
        if A[i][j] == -1:
            ans1 += 1
        if A[j][i] == -1:
            ans2 += 1
    if ans1 == 3 or ans2 == 3:
        print("Yes")
        return

if (A[0][0] == -1 and A[1][1] == -1 and A[2][2] == -1) or \
        (A[0][2] == -1 and A[1][1] == -1 and A[2][0] == -1):
    print("Yes")
else:
    print("No")
