(n, m) = map(int, input().split())
ans = 0
if m >= 2 and n > 0:
    ans += min(n, m // 2)
    m -= 2 * ans
if m > 0:
    ans += m // 4
print(ans)
