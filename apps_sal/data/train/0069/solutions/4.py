for t in range(int(input())):
    a, b = list(map(int, input().split()))
    m = input()
    x = []
    i = 0
    while i < len(m) and m[i] == '0':
        i += 1
    cs = 0

    while i < len(m):
        if m[i] == '0':
            cs += 1
        if m[i] == '1' and cs != 0:
            x += [cs]
            cs = 0
        i += 1
    cp = (len(x) + 1) * a
    for i in x:
        if i * b < a:
            cp -= a
            cp += i * b
    if m == '0' * len(m):
        print(0)
    else:
        print(cp)
