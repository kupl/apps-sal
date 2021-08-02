m, n = [int(i) for i in input().split()]
r = m
for i in range(1, m):
    r -= (i / m)**n
print(r)
