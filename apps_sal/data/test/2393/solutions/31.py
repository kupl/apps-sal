t = int(input())
for i in range(t):
    a = input()
    an = 0
    nm = []
    if (len(a) > 2):
        v = 2
        if (a[v - 2] + a[v - 1] + a[v]) == 'one':
            an += 1
            nm.append(v)
        if (a[v - 2] + a[v - 1] + a[v]) == 'two':
            an += 1
            nm.append(v)
    if (len(a) > 3):
        v = 3
        if (a[v - 2] + a[v - 1] + a[v]) == 'one':
            an += 1
            nm.append(v)
        if (a[v - 2] + a[v - 1] + a[v]) == 'two':
            an += 1
            nm.append(v)
    for v in range(4, len(a)):
        if (a[v - 4] + a[v - 3] + a[v - 2] + a[v - 1] + a[v]) == 'twone':
            if len(nm) != 0:
                nm.pop()
            else:
                an += 1
            nm.append(v - 1)
        elif (a[v - 2] + a[v - 1] + a[v]) == 'one':
            an += 1
            nm.append(v)
        if (a[v - 2] + a[v - 1] + a[v]) == 'two':
            an += 1
            nm.append(v)
    print(an)
    print(*nm, sep=' ')
