(a, k) = input().split()
(a, k) = (list(a), int(k))
for (i, x) in enumerate(a):
    if k == 0:
        break
    (vi, v) = (-1, x)
    for (j, y) in enumerate(a[i + 1:min(len(a), i + k + 1)]):
        if y > v:
            (vi, v) = (j, y)
    if vi > -1:
        del a[i + vi + 1]
        a.insert(i, v)
        k -= vi + 1
print(''.join(a))
