n, m = list(map(int, input().split()))
a = [list(map(int, list(input()))) for _ in range(n)]

ans = "NO"
cnt = [0 for _ in range(m)]
for i in range(n):
    for j in range(m):
        cnt[j] += a[i][j]
for i in range(n):
    ok = True
    for j in range(m):
        if a[i][j] == 1 and cnt[j] == 1:
            ok = False
            break
    if ok:
        ans = "YES"
        break
print(ans)
