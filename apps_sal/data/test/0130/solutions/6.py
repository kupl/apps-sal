n, m = map(int, input().split())
s = [list(input()) for _ in range(n)]
u, d, l, r = 11**11, 0, 11**11, 0
for i in range(n):
    for j in range(m):
        if s[i][j] == 'B':
            if i < u:
                u = i
            if i > d:
                d = i
            if j < l:
                l = j
            if j > r:
                r = j
if r - l >= n or d - u >= m:
    print(-1)
elif u == 11**11 and d == 0 and l == 11**11 and r == 0:
    print(1)
else:
    ans = 0
    for i in range(u, d + 1):
        for j in range(l, r + 1):
            if s[i][j] == 'W':
                ans += 1
    print(ans + ((max(r - l + 1, d - u + 1) - min(r - l + 1, d - u + 1)) * (max(r - l + 1, d - u + 1))))
