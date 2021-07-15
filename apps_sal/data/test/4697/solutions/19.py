s, c = map(int, input().split())

if 2 * s <= c:
    ans = s
    c = c - 2 * s
else:
    ans = c // 2
    c = 0
if c >= 4:
    ans += c // 4
print(ans)
