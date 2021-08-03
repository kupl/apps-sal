a, b, c, d = map(int, input().split())
ans = [a * c, a * d, b * d, c * b]
print(max(ans))
