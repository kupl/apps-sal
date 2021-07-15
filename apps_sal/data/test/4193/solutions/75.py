a_str = [input().split() for _ in range(3)]
a = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(3):
    for j in range(3):
        a[i][j] = int(a_str[i][j])

n = int(input())
b = [int(input()) for _ in range(n)]

for m in range(n):
    for i in range(3):
        for j in range(3):
            if b[m] == a[i][j]:
                a[i][j] = 0

#横のビンゴ判定
for i in range(3):
    if a[i][0] == a[i][1] == a[i][2] == 0:
        print('Yes')
        return

#縦のビンゴ判定
for i in range(3):
    if a[0][i] == a[1][i] == a[2][i] == 0:
        print('Yes')
        return

#斜めのビンゴ判定
if a[0][0] == a[1][1] == a[2][2] == 0:
    print('Yes')
    return
if a[0][2] == a[1][1] == a[2][0] == 0:
    print('Yes')
    return

print('No')
