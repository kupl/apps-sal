a, b, c, x, y = list(map(int, input().split()))

m = min(x, y)
c2 = min(a + b, 2 * c)
ans = c2 * m
x -= m
y -= m
if x:
    ans += min(a, 2 * c) * x
if y:
    ans += min(b, 2 * c) * y
print(ans)
