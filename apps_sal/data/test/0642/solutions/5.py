a = list(map(int, input().split()))
if a[1] == 0:
    print('YES')
else:
    m = list(map(int, input().split()))
    m.sort()
    (Max, c) = (0, 1)
    if m[0] != 1 and m[-1] != a[0]:
        for i in range(len(m) - 1):
            if m[i] == m[i + 1] - 1:
                c += 1
                if c > Max:
                    Max = c
            else:
                c = 1
        if Max < 3:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')
