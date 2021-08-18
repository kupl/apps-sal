a = [list(map(int, input().split())) for _ in range(3)]
n = int(input())
b = [int(input()) for _ in range(n)]
# 行の判定
for i in range(3):
    for j in range(3):
        if a[i][j] not in b:
            break
        elif j == 2:
            print("Yes")
            return
# 列の判定
for i in range(3):
    for j in range(3):
        if a[j][i] not in b:
            break
        elif j == 2:
            print("Yes")
            return
# ななめの判定
if a[0][0] in b and a[1][1] in b and a[2][2] in b:
    print("Yes")
    return
if a[0][2] in b and a[1][1] in b and a[2][0] in b:
    print("Yes")
    return
print("No")
