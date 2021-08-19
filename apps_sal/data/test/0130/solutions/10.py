(n, m) = list(map(int, input().split()))
sq = [list(input()) for _ in range(n)]
rmin = n
rmax = 0
cmin = m
cmax = 0
cnt = 0
for r in range(n):
    for c in range(m):
        if sq[r][c] == 'B':
            cnt += 1
            rmin = min(rmin, r)
            rmax = max(rmax, r)
            cmin = min(cmin, c)
            cmax = max(cmax, c)
l = max(max(rmax - rmin + 1, cmax - cmin + 1), 1)
if min(n, m) < l:
    ans = -1
else:
    ans = l * l - cnt
print(ans)
