(N, M) = map(int, input().split(' '))
if M == 0:
    if N == 1:
        print(0)
    else:
        print('1', '0' * (N - 1), sep='')
else:
    is_end = False
    rst = [''] * N
    for i in range(M):
        (s, c) = input().split(' ')
        idx = int(s) - 1
        if idx == 0 and N != 1 and (c == '0'):
            print(-1)
            is_end = True
            break
        elif rst[idx] == '':
            rst[idx] = c
        elif rst[idx] != c:
            print(-1)
            is_end = True
            break
    if not is_end:
        for (i, j) in enumerate(rst):
            if i == 0 and j == '':
                print('1', end='')
            elif j == '':
                print('0', end='')
            else:
                print(j, end='')
