m, n = tuple(map(int, input().split()))

ans = 0
for x in range(1, m + 1):
    ans += x * ((x / m)**n - ((x - 1) / m)**n)
print('%0.9f' % ans)
