def f(c):
    return 'mps'.index(c)


l = [[], [], []]
for c in input().split():
    (a, b) = c
    l[f(b)].append(int(a))
for i in range(3):
    l[i].sort()
res = 3
for x in l:
    if len(x) == 0:
        continue
    elif len(x) == 1:
        res = min(res, 2)
    elif len(x) == 3:
        if len(set(x)) == 1:
            res = min(res, 0)
            break
        if x[0] == x[1] - 1 and x[1] == x[2] - 1:
            res = min(res, 0)
            break
    res = min(res, 2)
    for i in range(len(x)):
        for j in range(i + 1, len(x)):
            if abs(x[i] - x[j]) <= 2:
                res = min(res, 1)
print(res)
