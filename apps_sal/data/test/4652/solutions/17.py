for _ in range(int(input())):
    n = int(input())
    p = list((int(a) for a in input().split()))
    c = 0
    if p[n - 1] < p[0]:
        c += 1
    for i in range(1, n):
        if p[i - 1] < p[i]:
            c += 1
    if c == n - 1 or c == 1:
        print('YES')
    else:
        print('NO')
