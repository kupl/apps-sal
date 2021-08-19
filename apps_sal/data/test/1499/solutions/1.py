(n, m) = map(int, input().split())
a = [[] for i in range(4)]
for i in range(4 * n):
    cur = i + 1 if i < m else -1
    if len(a[0]) < n or len(a[3]) < n:
        if len(a[0]) == len(a[3]):
            a[0].append(cur)
        else:
            a[3].append(cur)
    elif len(a[1]) == len(a[2]):
        a[1].append(cur)
    else:
        a[2].append(cur)
for v in a:
    v.reverse()
for i in range(n):
    for col in (1, 0, 2, 3):
        if a[col][-1] != -1:
            print(a[col][-1], end=' ')
        a[col].pop()
print()
