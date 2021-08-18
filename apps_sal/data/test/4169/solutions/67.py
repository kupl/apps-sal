from operator import itemgetter

n, m = map(int, input().split())
ab = [list(map(int, input().split())) for i in range(n)]
ab.sort()
i = 0
ans = 0
while m > 0:
    if ab[i][1] <= m:
        m -= ab[i][1]
        ans += ab[i][0] * ab[i][1]
    else:
        ans += ab[i][0] * m
        m = 0
    i += 1
print(ans)
