n, m = map(int, input().split())
M = [list(map(int, input().split())) for i in range(n)]
depth = [[1] * m for i in range(n)]
for col in range(m):
    for row in range(1, n):
        if M[row][col] >= M[row - 1][col]:
            depth[row][col] = depth[row - 1][col] + 1
max_depth = [max(row) for row in depth]
ans = ""
k = int(input())
for i in range(k):
    l, r = map(int, input().split())
    if max_depth[r - 1] >= r - l + 1:
        ans += "Yes\n"
    else:
        ans += "No\n"
print(ans)
