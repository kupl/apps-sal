def index(e, l, s):
    res = []
    off = s
    while True:
        try:
            off = l.index(e, off + 1)
        except ValueError:
            break
        else:
            res.append(off)
    if len(res) != 0:
        return res[0]
    else:
        return 10 ** 9


ni = list(map(int, input().strip().split(' ')))
n = ni[0]
k = ni[1]
arr = list(map(int, input().strip().split(' ')))
li = []
cost = 0
if k >= len(set(arr)):
    s = set(arr)
    print(len(s))
else:
    v = 1
    i = 1
    li.append(arr[0])
    while v < k and i < n:
        if arr[i] not in li:
            li.append(arr[i])
            v += 1
        i += 1
    cost = k
    for j in range(i, n):
        if arr[j] not in li:
            mi = 0
            for h in li:
                ind = index(h, arr, j)
                if ind > mi:
                    mi = ind
                    val = h
            li.remove(val)
            li.append(arr[j])
            cost += 1
    print(cost)
