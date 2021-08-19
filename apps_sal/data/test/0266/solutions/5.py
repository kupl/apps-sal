[m, s] = [int(s) for s in input().split()]
a = [0 for i in range(m)]
b = [0 for i in range(m)]
sa = s
i = m - 1
while i >= 0:
    if sa > 9:
        a[i] = 9
        sa = sa - 9
    else:
        a[i] = sa
        sa = 0
    i -= 1
fail = sa > 0
if not fail:
    if m > 1 and a[0] == 0:
        a[0] = 1
        found = False
        for i in range(1, m):
            if a[i] > 0:
                a[i] -= 1
                found = True
                break
        fail = not found
if fail:
    print(-1, -1)
else:
    sb = s
    for i in range(m):
        if sb > 9:
            b[i] = 9
            sb = sb - 9
        else:
            b[i] = sb
            sb = 0
    print('{0} {1}'.format(''.join(map(str, a)), ''.join(map(str, b))))
