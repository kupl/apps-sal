def __starting_point():
    n = int(input())
    c = input().split()
    t = input().split()
    for i in range(n):
        c[i] = int(c[i])
        t[i] = int(t[i])
    d = [0 for i in range(n - 1)]
    s = [0 for i in range(n - 1)]
    for i in range(n - 1):
        d[i] = c[i + 1] - c[i]
        s[i] = t[i + 1] - t[i]
    d.sort()
    s.sort()
    index = 0
    same = True
    while same and index < n - 1:
        if d[index] == s[index]:
            index += 1
        else:
            same = False
    if not c[0] == t[0]:
        same = False
    if not c[n - 1] == t[n - 1]:
        same = False
    if same:
        print('Yes')
    else:
        print('No')


__starting_point()
