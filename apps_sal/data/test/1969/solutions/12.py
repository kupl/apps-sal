n = int(input())
arr = []
for i in range(n):
    s = str(input())
    arr.append(s)
ans = 0
for i in range(1, n - 1):
    for j in range(1, n - 1):
        if(arr[i][j] == arr[i - 1][j - 1] == arr[i + 1][j + 1] == arr[i - 1][j + 1] == arr[i + 1][j - 1] == 'X'):
            ans += 1
print(ans)
