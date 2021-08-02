n, m = map(int, input().split())

ans = 0
if n * 2 <= m:
    ans += n
    m -= n * 2
else:
    ans += m // 2
    print(ans)
    return

if 4 <= m: ans += m // 4
print(ans)
