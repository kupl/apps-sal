q = int(input())
for re in range(q):
    n = int(input())
    (a, b, c) = list(map(int, input().split()))
    st = input()
    odp = [0] * n
    wyn = 0
    for i in range(n):
        if st[i] == 'R' and b > 0:
            wyn += 1
            b -= 1
            odp[i] = 'P'
        if st[i] == 'P' and c > 0:
            wyn += 1
            c -= 1
            odp[i] = 'S'
        if st[i] == 'S' and a > 0:
            wyn += 1
            a -= 1
            odp[i] = 'R'
    for i in range(n):
        if odp[i] == 0:
            if a > 0:
                a -= 1
                odp[i] = 'R'
            elif b > 0:
                b -= 1
                odp[i] = 'P'
            else:
                c -= 1
                odp[i] = 'S'
    if wyn >= (n + 1) // 2:
        print('YES')
        for i in range(n):
            if i < n - 1:
                print(odp[i], end='')
            else:
                print(odp[i])
    else:
        print('NO')
