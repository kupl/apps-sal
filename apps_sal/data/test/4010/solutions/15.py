t = int(input())
for x in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = {}
    for x in range(n):
        if a[x] in b:
            if b[a[x]][-1] != x - 1:
                b[a[x]].append(x)
        else: b[a[x]] = [x]
    t = False
    for x in b:
        if len(b[x]) >= 2:
            t = True
    if t:
        print('YES')
    else:
        print('NO')
