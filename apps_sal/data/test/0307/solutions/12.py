a, b, c, d = map(int, input().split())
mx = min(a, c, d)
ans = mx * 256 + min(a - mx, b) * 32
print(ans)
