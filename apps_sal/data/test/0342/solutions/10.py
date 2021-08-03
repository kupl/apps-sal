a, b, c = map(int, input().split())
res = 2 * c
x = min(a, b)
res += 2 * x
if a - x > 0:
    res += 1
if b - x > 0:
    res += 1
print(res)
