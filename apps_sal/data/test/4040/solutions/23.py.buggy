n, m, d = map(int, input().split())
c = list(map(int, input().split()))

boards = [None] * (m + 1)
boards[-1] = [n + 1, n + 1]
for i in range(m - 1, -1, -1):
    boards[i] = [boards[i + 1][0] - c[i], boards[i + 1][0] - 1]

pos = 0
for i in range(m + 1):
    if pos + 1 == boards[i][0]:
        pos = boards[i][1]
        continue
    if boards[i][0] <= pos + d <= n + 1:
        if pos + d <= boards[i][1]:
            pos = boards[i][1]
        continue
    diff = boards[i][0] - (pos + d)
    boards[i][0] -= diff
    boards[i][1] -= diff
    pos = boards[i][1]

if pos < n + 1:
    print('NO')
    return
else:
    ans = [0] * (n + 1)
    for i in range(m):
        for j in range(boards[i][0], boards[i][1] + 1):
            ans[j] = i + 1

    print('YES')
    print(*ans[1:])
