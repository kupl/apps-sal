(n, m) = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]
h = [[False for j in range(m)] for i in range(n)]
cnt = 0
for i in range(n):
    for j in range(m):
        h[i][j] = arr[i][j * 2] or arr[i][j * 2 + 1]
        if h[i][j]:
            cnt += 1
print(cnt)
