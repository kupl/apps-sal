a, b, c, d = map(int, input().split())
ans = max(a*c, b*d, a*d, b*c)
print(ans)
