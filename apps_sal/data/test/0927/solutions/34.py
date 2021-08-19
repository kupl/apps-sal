(N, M) = list(map(int, input().split()))
A = list(map(int, input().split()))
A.sort()
if 1 in A:
    if N % 2 == 0:
        print('1' * (N // 2))
    elif 7 in A:
        print('7' + '1' * (N // 2 - 1))
    elif 5 in A:
        print('5' + '1' * (N // 2 - 2))
    elif 3 in A:
        print('3' + '1' * (N // 2 - 2))
    elif 2 in A:
        print('2' + '1' * (N // 2 - 2))
    else:
        print('8' + '1' * (N // 2 - 3))
else:
    B = [[] for i in range(0, 10)]
    for i in range(0, M):
        if 2 in A:
            B[5].append(2)
        if 3 in A:
            B[5].append(3)
        if 4 in A:
            B[4].append(4)
        if 5 in A:
            B[5].append(5)
        if 6 in A:
            B[6].append(6)
        if 7 in A:
            B[3].append(7)
        if 8 in A:
            B[7].append(8)
        if 9 in A:
            B[6].append(9)
    dp = ['n' for i in range(0, max(10, N + 1))]
    for i in range(0, min(N + 1, 10)):
        if i == 2:
            if 2 in A:
                dp[5] = '2'
        if i == 3:
            if 3 in A:
                dp[5] = '3'
        if i == 4:
            if 4 in A:
                dp[4] = '4'
        if i == 5:
            if 5 in A:
                dp[5] = '5'
        if i == 6:
            if 6 in A:
                dp[6] = '6'
        if i == 7:
            if 7 in A:
                dp[3] = '7'
        if i == 8:
            if 8 in A:
                dp[7] = '8'
        if i == 9:
            if 9 in A:
                dp[6] = '9'
    if N >= 6:
        a = '0'
        b = '0'
        c = '0'
        if B[3] != []:
            b = '77'
        if dp[6] == 'n':
            a = int(a)
            b = int(b)
            c = int(c)
            x = max(a, b, c)
            if x != 0:
                dp[6] = str(x)
        else:
            a = int(a)
            b = int(b)
            c = int(c)
            d = int(dp[6])
            dp[6] = str(max(a, b, c, d))
    if N >= 7:
        a = '0'
        b = '0'
        c = '0'
        d = '0'
        if B[3] != [] and dp[4] != 'n':
            b = '7' + dp[4]
        if B[4] != [] and dp[3] != 'n':
            c = '47'
        if dp[7] == 'n':
            a = int(a)
            b = int(b)
            c = int(c)
            d = int(d)
            x = max(a, b, c, d)
            if x != 0:
                dp[7] = str(x)
        else:
            a = int(a)
            b = int(b)
            c = int(c)
            d = int(d)
            e = int(dp[7])
            dp[7] = str(max(e, a, b, c, d))
    for i in range(8, N + 1):
        a = '0'
        b = '0'
        c = '0'
        d = '0'
        e = '0'
        f = '0'
        if B[3] and dp[i - 3] != 'n':
            b = '7' + dp[i - 3]
        if B[4] and dp[i - 4] != 'n':
            c = '4' + dp[i - 4]
        if B[5] and dp[i - 5] != 'n':
            d = str(max(B[5])) + dp[i - 5]
        if B[6] and dp[i - 6] != 'n':
            e = str(max(B[6])) + dp[i - 6]
        if B[7] and dp[i - 7] != 'n':
            f = '8' + dp[i - 7]
        a = int(a)
        b = int(b)
        c = int(c)
        d = int(d)
        e = int(e)
        f = int(f)
        x = max(a, b, c, d, e, f)
        if x == 0:
            dp[i] = 'n'
        else:
            dp[i] = str(x)
    print(int(dp[N]))
