def resolve():
    (n, x) = map(int, input().split())
    ml = list()
    for i in range(n):
        m = int(input())
        ml.append(m)
    ml.sort()
    c = 0
    for g in ml:
        if x - g < 0:
            break
        else:
            c += 1
            x -= g
    a = int(x / ml[0])
    c += a
    print(c)


resolve()
