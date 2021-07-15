n = int(input())
point = [0] * (n + 1)
for i in range(n + 1):
    point[i] = [int(x) for x in input().split()]
v = [0] * n
for i in range(1, n + 1):
    v[i - 1] = [point[i][0] - point[i - 1][0], point[i][1] - point[i - 1][1]]
ans = 0
for i in range(1, n - 1):
    if v[i - 1][0] * v[i][1] - v[i - 1][1] * v[i][0] > 0:
        ans += 1
if v[n - 1][0] * v[0][1] - v[n - 1][1] * v[0][0] > 0:
    ans += 1
print(ans)
