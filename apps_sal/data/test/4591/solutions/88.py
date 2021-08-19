(a, b, c, x, y) = map(int, input().split())
c *= 2
ans = 10 ** 16
for i in range(max(x, y) + 1):
    m = 0
    m += a * max(0, x - i) + b * max(0, y - i) + c * i
    ans = min(ans, m)
print(ans)
