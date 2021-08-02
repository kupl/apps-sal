n, m = list(map(int, input().split()))
ab = [list(map(int, input().split())) for i in range(n)]

ab.sort()
ans = 0
for i in range(n):
    if m >= ab[i][1]:
        ans += ab[i][0] * ab[i][1]
        m = m - ab[i][1]
    elif 0 < m < ab[i][1]:
        ans += m * ab[i][0]
        break
print(ans)
