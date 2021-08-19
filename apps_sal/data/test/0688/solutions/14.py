t = [*map(int, input())]
s = [*map(int, input())]
d = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 6: 0, 7: 0, 8: 0}
di = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 6: 0, 7: 0, 8: 0}
for (i, x) in enumerate(t):
    if x == 6 or x == 9:
        d[6] += 1
    elif x == 2 or x == 5:
        d[2] += 1
    else:
        d[x] += 1
for (i, x) in enumerate(s):
    if x == 6 or x == 9:
        di[6] += 1
    elif x == 2 or x == 5:
        di[2] += 1
    else:
        di[x] += 1
res = 10000000000000000000000000
for (i, x) in enumerate(d):
    if d[x] > 0:
        res = min(res, di[x] // d[x])
print(res)
