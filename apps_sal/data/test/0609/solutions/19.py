n = int(input())
a = []
flag = 1
for i in range(0, n):
    a.append(input())
    for j in range(0, n):
        if i + j == n - 1 or i - j == 0:
            flag &= (a[-1][j] == a[0][0])
        else:
            flag &= (a[-1][j] == a[0][1]) & (a[-1][j] != a[0][0])
if flag:
    print("YES")
else:
    print("NO")
