n, m, c = map(int, input().split())
b = list(map(int, input().split()))
a = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for i in range(n):
    sum = 0

    for j in range(m):
        sum += a[i][j] * b [j]

    if sum + c > 0:
        ans += 1


print(ans)
