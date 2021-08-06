m, p = map(int, input().split())
fr = set()
arr = {}
for i in range(m):
    x, y = map(int, input().split())
    if x in arr:
        arr[x].append(y)
    else:
        arr[x] = [y]
    x, y = y, x
    if x in arr:
        arr[x].append(y)
    else:
        arr[x] = [y]
    fr.add((x, y))
    fr.add((y, x))
res = {}
for x, y in fr:
    res[x] = []
    res[y] = []
for i in arr:
    for j in arr:
        if i == j or (i, j) in fr:
            continue
        r = 0
        for k in arr:
            if i == k or j == k or (i, k) not in fr or (j, k) not in fr:
                continue
            r += 1
        if r * 100 >= p * len(arr[i]):
            res[i].append(j)
m = 0
for k in range(len(res)):
    i = 2 * 10 ** 9
    for j in res:
        if j > m and j < i:
            i = j
    m = i
    print(i, end=': ')
    print(len(res[i]), end=' ')
    res[i].sort()
    for j in res[i]:
        print(j, end=' ')
    print()
