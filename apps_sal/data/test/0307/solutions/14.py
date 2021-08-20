(a, b, c, d) = map(int, input().split())
ans = 0
ans += 256 * min(a, min(c, d))
left = a - ans // 256
ans += 32 * min(b, left)
print(ans)
