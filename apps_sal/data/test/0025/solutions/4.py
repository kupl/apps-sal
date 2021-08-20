(n, k) = list(map(int, input().split()))
if n * n < k:
    print(-1)
else:
    arr = [[0 for _ in range(n)] for _ in range(n)]
    cnt = 0
    for i in range(n):
        if cnt < k:
            arr[i][i] = 1
            cnt += 1
        for j in range(i + 1, n):
            if cnt <= k - 2:
                arr[i][j] = 1
                arr[j][i] = 1
                cnt += 2
    for r in arr:
        print(' '.join(map(str, r)))
