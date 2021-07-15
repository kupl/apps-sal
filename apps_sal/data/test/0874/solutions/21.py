n = int(input())
if n % 2:
    print(-1)
else:
    arr = list(range(1, n + 1))
    for i in range(0, n, 2):
        arr[i], arr[i + 1] = arr[i + 1], arr[i]
    print(*arr)

