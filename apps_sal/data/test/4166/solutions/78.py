(N, M) = map(int, input().split(' '))
rst = [''] * N
is_end = False
if M == 0:
    if N == 1:
        print(0)
    else:
        print('1', '0' * (N - 1), sep='')
else:
    for i in range(M):
        (s, c) = input().split(' ')
        if int(s) - 1 == 0 and N != 1 and (c == '0'):
            print(-1)
            is_end = True
            break
        elif rst[int(s) - 1] == '':
            rst[int(s) - 1] = c
        elif rst[int(s) - 1] != c:
            print(-1)
            is_end = True
            break
    if not is_end:
        for (i, j) in enumerate(rst):
            if i == 0 and j == '':
                print(1, end='')
            else:
                if j == '':
                    print(0, end='')
                print(j, end='')
