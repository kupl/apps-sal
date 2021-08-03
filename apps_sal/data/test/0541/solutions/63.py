n, m = list(map(int, input().split()))
ab = [list(map(int, input().split())) for i in range(m)]
ab.sort()
ans = 0
now = 1
for i in range(m):
    if now <= ab[i][0]:
        ans += 1
        now = ab[i][1]
    now = min(now, ab[i][1])
print(ans)
