for _ in range(int(input())):
    (n, k) = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    m = max(arr)
    for i in range(n):
        arr[i] = m - arr[i]
    k -= 1
    if k % 2 == 1:
        m = max(arr)
        for i in range(n):
            arr[i] = m - arr[i]
    print(*arr)
