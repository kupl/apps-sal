n = int(input())

lst = [int(x) for x in input().split()]

d = {}
for x in lst:
    if not x in d:
        d[x] = 0
    d[x] += 1

maxi = 0
for (x, y) in list(d.items()):
    maxi = max(maxi, y)

print(maxi)

