(n, a) = (int(input()), list(map(int, input().split())) + [0])
(ans, inc, dec) = ([0] * n, -1, 10000000.0)
for i in range(n):
    if inc < a[i] < dec:
        if a[i] < a[i + 1]:
            inc = a[i]
        else:
            dec = a[i]
            ans[i] = 1
    elif inc < a[i]:
        inc = a[i]
    elif dec > a[i]:
        dec = a[i]
        ans[i] = 1
    else:
        print('NO')
        break
else:
    print('YES')
    print(*ans)
