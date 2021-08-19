(a, b, c, d) = map(int, input().split())
ans = min(d - a, b - c, d - c, b - a)
print(max(ans, 0))
