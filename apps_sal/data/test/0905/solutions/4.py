n, s = [int(st) for st in input().split()]
res = -1
for i in range(n):
    x, y = [int(st) for st in input().split()]
    if ((x + y / 100) <= s):
        if (y == 0):
            y = 100
        res = max(res, 100 - y)
print(res)
