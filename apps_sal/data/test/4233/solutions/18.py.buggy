n, m = map(int, input().split())
sky = [0] * (n + 1)
for i in range(n):
    sky[i] = list(input()) + ['.']
sky[n] = ['.'] * m
used = [[False] * m for i in range(n)]
ans = []
for i in range(n):
    for j in range(m):
        if sky[i][j] == '.':
            continue
        ln = 1
        while sky[i - ln][j] == '*' and sky[i + ln][j] == '*' and sky[i][j - ln] == '*' and sky[i][j + ln] == '*':
            used[i - ln][j] = used[i + ln][j] = used[i][j - ln] = used[i][j + ln] = True
            ln += 1
        if ln > 1:
            used[i][j] = True
            ans += [[i + 1, j + 1, ln - 1]]
for i in range(n):
    for j in range(m):
        if sky[i][j] == '*' and not used[i][j]:
            print(-1)
            return
print(len(ans))
for i in range(len(ans)):
    print(*ans[i])
