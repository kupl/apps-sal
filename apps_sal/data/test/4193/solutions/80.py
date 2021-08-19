a = [input().split() for _ in range(3)]
n = int(input())
b = [input() for _ in range(n)]
for i in range(3):
    for j in range(3):
        for k in range(n):
            if a[i][j] == b[k]:
                a[i][j] = '0'
ans = 'No'
for i in range(3):
    if a[i][0] == a[i][1] == a[i][2]:
        ans = 'Yes'
    if a[0][i] == a[1][i] == a[2][i]:
        ans = 'Yes'
if a[0][0] == a[1][1] == a[2][2]:
    ans = 'Yes'
if a[0][2] == a[1][1] == a[2][0]:
    ans = 'Yes'
print(ans)
