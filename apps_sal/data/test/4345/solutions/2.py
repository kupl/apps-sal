n, a = int(input()), [int(ai) for ai in input().split()] + [0]
res, inc, dec = [0] * n, -1, 10**6
for i in range(n):
    if inc < a[i] and a[i] < dec:
        if a[i] < a[i + 1]:
            inc = a[i]
        else:
            dec = a[i]
            res[i] = 1
    elif inc < a[i]:
        inc = a[i]
    elif dec > a[i]:
        dec = a[i]
        res[i] = 1
    else:
        print('NO')
        break
else:
    print('YES')
    print(*res)

