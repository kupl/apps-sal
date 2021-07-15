a, b, c = map(int, input().split())
m = min(a, b)
a -= m
b -= m
ans = c * 2 + m * 2 + min(1, max(a, b))
print(ans)
