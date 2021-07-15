a, b = map(int, input().split())
c, d = map(int, input().split())
mn = min(a * d, b * c)
mx = max(a * d, b * c)
x = 10 ** 18
if (a + b + c + d) != 0:
    x = abs((b * c - a * d) / (a + b + c + d))
if (a + b - c - d) != 0:
    x = min(abs((b * c - a * d) / (a + b - c - d)), x)
if (a - b + c - d) != 0:
    x = min(abs((b * c - a * d) / (a - b + c - d)), x)
if (a - b - c + d) != 0:
    x = min(abs((b * c - a * d) / (a - b - c + d)), x)
if (a + b + c + d) == 0:
    x = 0


print(x)
