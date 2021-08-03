n, m = map(int, input().split())
L = [list(map(int, input().split())) for _ in range(n)]
L = sorted(L, key=lambda x: x[0])
limit = m
ans = 0
for i in range(n):
    if limit <= 0:
        break
    ans += min(limit, L[i][1]) * L[i][0]
    limit -= L[i][1]
print(ans)
