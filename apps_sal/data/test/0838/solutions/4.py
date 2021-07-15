n, m = list(map(int, input().split()))
d = [list(map(int, input().split())) for i in range(n)]

ans = 0
for p in d:
    x = sum(p)
    ans += pow(2, x) + pow(2, m - x) - 2 - m

for i in range(m):
    x = sum(d[j][i] for j in range(n))
    ans += pow(2, x) + pow(2, n - x) - 2

print(ans)

