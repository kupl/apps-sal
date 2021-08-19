(a, b, c, d) = map(int, input().split())
ans = 0
if b <= c or d <= a:
    ans = 0
else:
    ans = min(d, b) - max(a, c)
print(ans)
