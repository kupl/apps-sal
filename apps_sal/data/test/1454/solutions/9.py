(n, m) = list(map(int, input().split()))
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
ans = 0
for i in range(n - 1, -1, -1):
    for j in range(m - 1, -1, -1):
        if arr[i][j] == 0:
            if i < n - 1 and j < m - 1:
                arr[i][j] = min(arr[i + 1][j], arr[i][j + 1]) - 1
            elif j < m - 1:
                arr[i][j] = arr[i][j + 1] - 1
            else:
                arr[i][j] = arr[i + 1][j] - 1
        ans += arr[i][j]
flag = True
for i in range(n):
    for j in range(m):
        if i < n - 1 and j < m - 1:
            if arr[i][j] >= arr[i][j + 1] or arr[i][j] >= arr[i + 1][j] or arr[i][j] >= arr[i + 1][j + 1]:
                flag = False
                break
        if i < n - 1:
            if arr[i][j] >= arr[i + 1][j]:
                flag = False
                break
        if j < m - 1:
            if arr[i][j] >= arr[i][j + 1]:
                flag = False
                break
    if flag:
        pass
    else:
        break
if flag:
    print(ans)
else:
    print(-1)
