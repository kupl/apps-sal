def solve():
    n = int(input())
    p = [int(x) for x in (input().split())]
    c = dict()
    cnt = 0
    for i in range(n):
        if i == 0:
            cnt += 1
            continue
        if p[i] == p[i - 1]:
            cnt += 1
        if p[i] != p[i - 1]:
            c[cnt] = 1
            cnt = 1
        if i == n - 1:
            c[cnt] = 1
    if len(c) < 2:
        print('YES')
    else:
        print('NO')


solve()
