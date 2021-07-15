t = int(input())
bo = []
for i in range(t):
    n = int(input())
    mr = 0
    b = [-2] * n
    l = []
    r = []
    for j in range(n):
        x, y = map(int, input().split())
        if y > mr:
            mr = y
        l.append(x)
        r.append(y)
    j = 1
    k = 0
    h = 0
    while j <= mr:
        if k < n and l[k] == j:
            b[k] = -1
            k += 1
            continue
        for o in range(n):
            if b[o] == -1:
                b[o] = j
                break
        for o in range(n):
            if r[o] == j and b[o] == -1:
                b[o] = 0
        j += 1
    bo.append(b)
for i in range(t):
    print(' '.join(map(str, bo[i])))
