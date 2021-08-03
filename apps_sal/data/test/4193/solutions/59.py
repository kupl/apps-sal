L = [list(map(int, input().split())) for _ in range(3)]
n = int(input())
B = list(int(input()) for _ in range(n))
ans = 'No'
for i in range(3):
    for j in range(3):
        for b in B:
            if L[i][j] == b:
                L[i][j] = 0

for i in range(3):
    if L[i][0] == L[i][1] == L[i][2] == 0:
        ans = 'Yes'  # 横
    if L[0][i] == L[1][i] == L[2][i] == 0:
        ans = 'Yes'  # 縦
if L[0][0] == L[1][1] == L[2][2] == 0:
    ans = 'Yes'
if L[0][2] == L[1][1] == L[2][0] == 0:
    ans = 'Yes'

print(ans)
