x, n = map(int, input().split())
d = 1
res = 0
while d < n ** 0.5:
    if n % d == 0 and d <= x and n // d <= x:
        res += 2
    d += 1
if d * d == n and d <= x:
    res += 1
print(res)
