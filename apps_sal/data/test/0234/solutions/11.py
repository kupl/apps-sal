n, m = list(map(int, input().split()))
f = [list(input()) for _ in range(n)]

ans = "YES"
cnt = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        if f[i][j] != '*':
            continue
        for di in range(-1, 2):
            for dj in range(-1, 2):
                if 0 < abs(di) + abs(dj) and 0 <= i + di < n and 0 <= j + dj < m:
                    cnt[i + di][j + dj] += 1
for i in range(n):
    for j in range(m):
        if f[i][j] == '.':
            if cnt[i][j] != 0:
                ans = "NO"
        elif f[i][j] != '*':
            if cnt[i][j] != int(f[i][j]):
                ans = "NO"
print(ans)
