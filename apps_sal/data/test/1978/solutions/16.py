def warshall_floyd(d):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d


n = int(input())
g = [list(input()) for _ in range(n)]
d = [[float('inf')] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if g[i][j] == '1':
            d[i][j] = 1
warshall_floyd(d)
m = int(input())
arr = list(map(int, input().split()))
for i in range(m):
    arr[i] -= 1
ans = [arr[0]]
pos1 = 0
pos2 = 1
pos3 = 2
for i in range(m - 2):
    (a, b, c) = (arr[pos1], arr[pos2], arr[pos3])
    if a != c:
        if d[a][b] + d[b][c] > d[a][c]:
            ans.append(b)
            pos1 = pos2
            pos2 = pos1 + 1
            pos3 = pos2 + 1
        else:
            pos2 += 1
            pos3 += 1
    elif d[a][b] + d[b][c] >= d[a][c]:
        ans.append(b)
        pos1 = pos2
        pos2 = pos1 + 1
        pos3 = pos2 + 1
    else:
        pos2 += 1
        pos3 += 1
ans.append(arr[-1])
l = len(ans)
for i in range(l):
    ans[i] += 1
print(l)
print(*ans)
