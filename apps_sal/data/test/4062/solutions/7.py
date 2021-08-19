(a, b, c, d) = map(int, input().split())
x1 = a * c
x2 = a * d
x3 = b * c
x4 = b * d
ans = max(x1, x2, x3, x4)
print(ans)
