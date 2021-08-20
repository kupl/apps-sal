(n, m) = map(int, input().split())
ans = 0
if m >= 2 and n >= 1:
    if m // 2 >= n:
        ans += n
        m = m - n * 2
        ans += m // 4
    else:
        ans += m // 2
print(ans)
