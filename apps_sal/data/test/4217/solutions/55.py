(n, m) = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
x = [0] * m
for i in range(n):
    for j in range(1, a[i][0] + 1):
        for k in range(1, 31):
            if a[i][j] == k:
                x[k - 1] += 1
ans = 0
for l in x:
    if l == n:
        ans += 1
print(ans)
