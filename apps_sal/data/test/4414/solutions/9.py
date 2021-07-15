q = int(input())
while q:
    a, b, n, s = [int(x) for x in input().split()]
    s -= min((s//n), a)*n
    if s <= b:
        print('YES')
    else:
        print('NO')
    q -= 1
