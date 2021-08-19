(n, m) = map(int, input().split())
if n == 0:
    print('0 1\n0 ' + str(m) + '\n0 0\n0 ' + str(m - 1))
elif m == 0:
    print('1 0\n' + str(n) + ' 0\n0 0\n' + str(n - 1) + ' 0')
elif n < m:
    if (n ** 2 + m ** 2) ** 0.5 + m < 2 * ((n - 1) ** 2 + m ** 2) ** 0.5:
        print(str(n - 1) + ' ' + str(m) + '\n0 0\n' + str(n) + ' ' + str(m) + '\n1 0')
    else:
        print('0 0\n' + str(n) + ' ' + str(m) + '\n' + str(n) + ' 0\n0 ' + str(m))
elif (n ** 2 + m ** 2) ** 0.5 + n < 2 * (n ** 2 + (m - 1) ** 2) ** 0.5:
    print(str(n) + ' ' + str(m - 1) + '\n0 0\n' + str(n) + ' ' + str(m) + '\n0 1')
else:
    print('0 0\n' + str(n) + ' ' + str(m) + '\n0 ' + str(m) + '\n' + str(n) + ' 0')
