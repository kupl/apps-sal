

n, d, h = list(map(int, input().split()))
if 2 * h < d:
    print(-1)
    return
j = 1
if d == 1:
    if n == 2:
        print(1, 2)
        return
    print(-1)
    return
if d == 2:
    if h == 1:
        for i in range(2, n + 1):
            print(1, i)
        return
    else:
        print(1, 2)
        print(2, 3)
        for i in range(4, n + 1):
            print(2, i)
        return
if h != d:
    for i in range(2, n + 1):
        if i - 1 < h + 1:
            print(i - 1, i)
            continue
        if h < d:
            print(j, i)
            j = i
            h += 1
            continue
        print(1, i)
    return
else:
    for i in range(2, n + 1):
        if i - 1 < h + 1:
            print(i - 1, i)
            continue
        print(2, i)

