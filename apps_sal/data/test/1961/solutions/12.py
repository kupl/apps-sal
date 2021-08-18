from math import ceil, sqrt

t = 1
for test in range(1, t + 1):
    n, m = (list(map(int, input().split())))
    arr = [["." for i in range(m)] for i in range(n)]
    arr2 = []
    for i in range(n):
        arr2.append(list(input()))
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if arr2[i + 1][j] == arr2[i][j + 1] == arr2[i + 1][j + 1] == arr2[i - 1][j] == arr2[i][j - 1] == arr2[i - 1][j - 1] == arr2[i + 1][j - 1] == arr2[i - 1][j + 1] == "
            arr[i + 1][j] = arr[i][j + 1] = arr[i + 1][j + 1] = arr[i - 1][j] = arr[i][j - 1] = arr[i - 1][j - 1] = arr[i + 1][j - 1] = arr[i - 1][j + 1] = "

    if arr == arr2:
        print("YES")
    else:
        print("NO")
