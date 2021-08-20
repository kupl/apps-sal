t = int(input())
for i in range(t):
    a = int(input())
    (x, y) = (0, 0)
    l = []
    for i in range(a):
        (x1, y1) = map(int, input().split())
        l.append([x1, y1])
    l.sort()
    ll = 0
    ch = 1
    for i in range(1, a):
        if l[i][1] < l[i - 1][1]:
            ch = 0
            break
    if ch == 0:
        print('NO')
    else:
        print('YES')
        st = ''
        for i in l:
            st += 'R' * (i[0] - x)
            x = i[0]
            st += 'U' * (i[1] - y)
            y = i[1]
        print(st)
