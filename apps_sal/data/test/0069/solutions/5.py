t = int(input())
for i in ' ' * t:
    n, x = map(int, input().split())
    s = input()
    L = [0]
    for i in s:
        if i == '0':
            L.append(L[-1] + 1)
        else:
            L.append(L[-1] - 1)
    k = L.pop()
    c = 0
    if k > 0:
        for i in L:
            if i % k == x % k and i <= x: c += 1
        print(c)
    elif k < 0:
        for i in L:
            if i % k == x % k and i >= x: c += 1
        print(c)
    else:
        for i in L:
            if i == x: c = -1
        print(c)
