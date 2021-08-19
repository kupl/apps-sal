(n, m, t) = list(map(int, input().split()))
go = []
for i in range(n):
    go.append(input())
cnt = 0
for j in range(m):
    x = 0
    for i in range(n):
        if go[i][j] == 'Y':
            x += 1
    if x >= t:
        cnt += 1
print(cnt)
