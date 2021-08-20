(n, m) = map(int, input().split())
ans = 0
if m - n * 2 > 0:
    ans += n
    tmp = m - n * 2
    ans += tmp // 4
else:
    ans += m // 2
print(ans)
