xs = [int(x) for x in input().split()]
res = 0
for i in range(14):
    newxs = xs[:]
    newxs[i] = 0
    for j in range(14):
        newxs[j] += xs[i] // 14
    for j in range(xs[i] % 14):
        newxs[(i + 1 + j) % 14] += 1
    res = max(res, sum((val for val in newxs if val % 2 == 0)))
print(res)
