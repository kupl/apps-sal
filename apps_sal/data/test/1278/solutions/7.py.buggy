n, x, y = list(map(int, input().split()))
arr = list(map(int, input().split()))
for i in range(n):
    flag = 0
    for j in range(i - 1, max(i - x - 1, -1), -1):
        if(arr[j] <= arr[i]):
            flag = 1

    for j in range(i + 1, min(i + y + 1, n)):
        if(arr[j] <= arr[i]):
            flag = 1
    if(flag == 0):
        print(i + 1)
        return
