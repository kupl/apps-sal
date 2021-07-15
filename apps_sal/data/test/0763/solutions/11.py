n = int(input())
p = [int(k) for k in input().split()]

res = None
best = None
for x in range(1, n + 1):
    cur = 0
    for i, v in enumerate(p):
        cur += v * (abs(x - (i + 1)) + i + (x - 1) + x - 1 + i + abs(x - (i + 1)))
    if res is None or cur < res:
        res = cur
        best = x
print(res)
