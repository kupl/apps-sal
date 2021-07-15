n, T = list(map(int, input().split()))
a = [[0 for _ in range(n)] for __ in range(n)]
for t in range(T):
    i, j = 0, 0
    a[i][j] += 1024
    for i in range(n - 1):
        for j in range(i + 1):
            if a[i][j] > 1024:
                diff = a[i][j] - 1024
                a[i][j] = 1024
                a[i + 1][j] += diff//2
                a[i + 1][j + 1] += diff//2
                if (diff % 2 != 0):
                    raise RuntimeError('whut')
ans = 0
for i in range(n):
    for j in range(i + 1):
        if a[i][j] >= 1024:
            ans += 1
print(ans)

