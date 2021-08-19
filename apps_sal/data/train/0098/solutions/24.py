q = int(input())
for _ in range(q):
    (c, m, x) = map(int, input().split())
    if c < m:
        (c, m, x) = (c, c, x + m - c)
    elif c > m:
        (c, m, x) = (m, m, x + c - m)
    ans = min(c, m, x)
    if c > x:
        ans += 2 * (c - x) // 3
    print(ans)
