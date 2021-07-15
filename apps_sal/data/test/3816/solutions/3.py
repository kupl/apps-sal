a, b, c, l = map(int, input().split())
ans = (l + 3) * (l + 2) // 2 * (l + 1) // 3
for z in (a, b, c):
    s = 2 * z - a - b - c
    for x in range(l + 1):
        m = min(s + x, l - x)
        if m >= 0:
            ans -= (m + 1) * (m + 2) >> 1
print(ans)
