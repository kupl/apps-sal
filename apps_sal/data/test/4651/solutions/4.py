t = int(input())
for tt in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    visited = [0] * n
    index = [0] * (n + 1)
    for i in range(1, n + 1):
        index[i] = arr.index(i)
    for i in range(1, n + 1):
        for j in range(index[i], 0, -1):
            if visited[j] == 0 and arr[j - 1] > arr[j]:
                temp = arr[j]
                arr[j] = arr[j - 1]
                arr[j - 1] = temp
                visited[j] += 1
    for i in arr:
        print(i, end=' ')
    print()
