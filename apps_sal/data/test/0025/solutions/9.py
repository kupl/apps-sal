n, k = list(map(int, input().split()))
a = [[0 for j in range(n)]for i in range(n)]
if n * n < k:
    print(-1)
    return
for i in range(n):
    cur = 2 * (n - i) - 1
    if cur <= k:
        k -= cur
        for j in range(i, n):
            a[i][j] = 1
            a[j][i] = 1
    else:
        if k == 0:
            break
        if k == 1:
            a[i][i] = 1
            break
        for j in range(i, i + (k + 1) // 2):
            a[i][j] = 1
            a[j][i] = 1
        if not k % 2:
            a[i + 1][i + 1] = 1
        break
        
for i in a:
    print(*i)
    

