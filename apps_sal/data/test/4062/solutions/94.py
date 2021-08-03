a, b, c, d = map(int, input().split())
l = [a * c, b * d, b * c, a * d]
print(max(l))
