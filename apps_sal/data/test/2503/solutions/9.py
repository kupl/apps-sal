(n, k) = map(int, input().split())
s = [[0] * k for _ in range(2 * k + 1)]
for _ in range(n):
    (x, y, c) = input().split()
    (x, y) = (int(x), int(y))
    x -= x // (2 * k) * (2 * k)
    y -= y // (2 * k) * (2 * k)
    if x >= k and y >= k:
        x -= k
        y -= k
    elif y >= k:
        x += k
        y -= k
    if c == 'B':
        if x >= k:
            x -= k
        else:
            x += k
    s[x + 1][y] += 1
for i in range(2 * k):
    for j in range(k):
        s[i + 1][j] += s[i][j]
ans = 0
for i in range(k):
    cnt = 0
    for j in range(k):
        cnt += s[i + k][j] - s[i][j]
    ans = max(ans, cnt, n - cnt)
    for j in range(k):
        cnt -= 2 * (s[i + k][j] - s[i][j])
        cnt += s[2 * k][j]
        ans = max(ans, cnt, n - cnt)
print(ans)
