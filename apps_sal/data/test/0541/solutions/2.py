n, m = map(int, input().split())
c = [[0] * 2 for _ in range(m)]
for i in range(m):
    c[i][1], c[i][0] = map(int, input().split())
c.sort()
x = -1
ans = 0
for i in range(m):
    if c[i][1] > x:
        x = c[i][0] - 1
        ans += 1
print(ans)
