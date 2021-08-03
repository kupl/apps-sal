n, m = list(map(int, input().split()))
ab = [list(map(int, input().split())) for _ in range(m)]

ab.sort(key=lambda x: x[1])

ans = m
for i in range(1, m):
    if ab[i][0] < ab[i - 1][1]:
        ab[i][1] = ab[i - 1][1]
        ans -= 1
print(ans)
