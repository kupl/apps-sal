t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    grow = shrink = False
    for ai, bi in zip(a, b):
        if bi < ai:
            if not shrink:
                print('NO')
                break
        elif bi > ai and not grow:
            print('NO')
            break
        if ai == 1:
            grow = True
        elif ai == -1:
            shrink = True
    else:
        print('YES')
