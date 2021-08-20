(a, b, c, d) = map(int, input().split())
ans = max(max(a * c, a * d), max(b * c, b * d))
print(ans)
