a, b, c, d = map(int, input().split())
ans = min(b, d) - max(a, c)
print((ans, 0)[ans < 0])
