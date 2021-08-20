(n, m) = map(int, input().split())
(mn, mx) = (-1, 10 ** 7)
for _ in range(m):
    (l, r) = map(int, input().split())
    mn = max(mn, l)
    mx = min(mx, r)
ans = max(mx - mn + 1, 0)
print(ans)
