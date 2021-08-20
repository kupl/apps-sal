for _ in range(int(input())):
    n = int(input())
    p = []
    for _ in range(n):
        (x, y) = map(int, input().split())
        p.append((x, y))
    p.sort()
    (x, y) = (0, 0)
    ans = ''
    while p:
        ans += 'R' * (p[0][0] - x)
        if p[0][1] < y:
            print('NO')
            break
        ans += 'U' * (p[0][1] - y)
        (x, y) = p[0]
        p.pop(0)
    else:
        print('YES', ans, sep='\n')
