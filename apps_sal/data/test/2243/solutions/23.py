(n, k, q) = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
b = [0]
for i in range(q):
    (t, d) = [int(x) for x in input().split()]
    if t == 2:
        if d in b:
            print('YES')
        else:
            print('NO')
    if b[0] == 0:
        b.remove(0)
        b.append(d)
    if t == 1:
        for y in range(len(b)):
            if a[d - 1] > a[b[y] - 1]:
                b.insert(y, d)
                break
        if a[d - 1] < a[b[len(b) - 1] - 1]:
            b.append(d)
        if len(b) == k + 1:
            b.pop(len(b) - 1)
