n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
if arr[0][0] == 1 or arr[0][m - 1] == 1 or arr[n - 1][0] == 1 or arr[n - 1][m - 1] == 1:
    print(1)
else:
    flag = 0
    for i in range(n):
        if arr[i][0] == 1:
            flag = 1
        if arr[i][m - 1] == 1:
            flag = 1
    for i in range(m):
        if arr[0][i] == 1:
            flag = 1
        if arr[n - 1][i] == 1:
            flag = 1
    if flag == 1:
        print(2)
    else:
        print(4)
