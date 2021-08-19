def __starting_point():
    n = int(input())
    a = list(map(int, input().split()))
    possible = True
    prev = 0
    for i in range(n):
        v = a[i] - prev
        if v < 0:
            possible = False
        v %= 2
        prev = v
    if prev == 0 and possible:
        print('YES')
    else:
        print('NO')


__starting_point()
