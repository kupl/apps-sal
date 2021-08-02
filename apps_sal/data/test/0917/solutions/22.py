n, h, m = [int(x) for x in input().split(' ')]

dollars = 0
houses = [h] * n
for i in range(m):
    l, r, x = [int(x) for x in input().split(' ')]
    for j in range(l, r + 1):
        houses[j - 1] = min(x, houses[j - 1])

print(sum([a * a for a in houses]))
