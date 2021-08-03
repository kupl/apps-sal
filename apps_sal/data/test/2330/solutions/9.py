t = int(input())
for i in range(t):
    n, m = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    if arr[0] < arr[1]:
        min1 = arr[0]
        index1 = 1
        min2 = arr[1]
        index2 = 2
    else:
        min1 = arr[1]
        min2 = arr[0]
        index1 = 2
        index2 = 1
    for j in range(2, n):
        if arr[j] < min2:
            if arr[j] < min1:
                min1 = arr[j]
                index1 = j + 1
            else:
                min2 = arr[j]
                index2 = j + 1
    if m < n or n == 2:
        print(-1)
    else:
        ans = sum(arr) * 2 + (m - n) * (min1 + min2)
        print(ans)
        for j in range(1, n):
            print(j, j + 1)
        print(1, n)
        for j in range(m - n):
            print(index1, index2)
