for _ in range(int(input())):
    p1 = 0
    c1 = 0
    flag = True
    for _ in range(int(input())):
        (p2, c2) = list(map(int, input().split()))
        if not flag:
            continue
        if p2 < p1 or c2 < c1:
            flag = False
        if p2 - p1 < c2 - c1:
            flag = False
        p1 = p2
        c1 = c2
    if flag:
        print('YES')
    else:
        print('NO')
