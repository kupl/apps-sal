(n, m) = [int(x) for x in input().split()]
d = []
found = False
if m != 0:
    d = [int(x) for x in input().split()]
    d.sort()
    if d[0] == 1 or d[m - 1] == n:
        print('NO')
        found = True
if not found:
    found = False
    for i in range(2, m):
        if d[i - 2] == d[i] - 2 and d[i - 1] == d[i] - 1:
            found = True
            print('NO')
            break
    if not found:
        print('YES')
