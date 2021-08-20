n = int(input())
data = [list(map(int, input().split())) for i in range(n + 1)]
ans = 0
for i in range(n - 3):
    (x0, y0, x1, y1, x2, y2) = (data[i][0], data[i][1], data[i + 1][0], data[i + 1][1], data[i + 2][0], data[i + 2][1])
    if y0 == y1 and x1 == x2:
        ans += 1
print(ans)
