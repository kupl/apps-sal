a = [list(map(int ,input().split())) for _ in range(3)]
n = int(input())

ans = [[0] * 3 for _ in range(3)]

for i in range(n):
    b = int(input())
    for j in range(3):
        for k in range(3):
            if a[j][k] ==  b:
                ans[j][k] = 1

state = False
for i in range(3):
    num = 0
    for j in range(3):
        num += ans[i][j]
    
    if num == 3:
        state = True

for i in range(3):
    num = 0
    for j in range(3):
        num += ans[j][i]
    
    if num == 3:
        state = True

if ans[0][0] + ans[1][1] + ans[2][2] == 3:
    state = True

if ans[0][2] + ans[1][1] + ans[2][0] == 3:
    state = True

if state:
    print("Yes")
else:
    print("No")


