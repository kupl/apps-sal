t = int(input())
for _ in range(t):
    (n, k) = list(map(int, input().split()))
    arr = [int(j) for j in input().split()]
    ma = max(arr)
    for i in range(n):
        arr[i] = ma - arr[i]
    k -= 1
    if k % 2 == 0:
        print(*arr)
    else:
        ma = max(arr)
        for i in range(n):
            arr[i] = ma - arr[i]
        print(*arr)
