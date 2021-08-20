(n, m) = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]
ans = 0
for i in arr:
    for k in range(m):
        if i[2 * k + 1] == 1 or i[2 * k] == 1:
            ans += 1
print(ans)
