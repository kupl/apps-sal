m, n = [int(x) for x in input().split()]

ans = m
for i in range(1, m):
    ans -= (i / m)**n

print("%0.10f" % ans)
