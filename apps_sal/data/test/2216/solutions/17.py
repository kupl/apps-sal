def addX(x, y):
    if y % 2 == 0:
        x += 1
        if x == m:
            y += 1
            x -= 1
    else:
        x -= 1
        if x == -1:
            y += 1
            x += 1
    return x, y


n, m, k = [int(x) for x in input().split()]
res = []
curx, cury, curk, curlen = 0, 0, 0, 0
for i in range(k - 1):
    res.append([])
    for j in range(2):
        res[i].append([cury + 1, curx + 1])
        curx, cury = addX(curx, cury)
res.append([])
while cury < n:
    res[k - 1].append([cury + 1, curx + 1])
    curx, cury = addX(curx, cury)
print('\n'.join(str(len(x)) + ' ' + ' '.join(' '.join(list(map(str, y))) for y in x) for x in res))
# print(res)
